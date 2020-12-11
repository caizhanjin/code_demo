def go_draw_prize(request):
    """
    开始抽奖，分两步：
    1. 创建抽奖记录
    2. 进行抽奖
    """
    if request.method != "GET":
        return ReturnDataApi(msg="请求方式不存在", code=404)
    request_data = request.GET.copy()

    activity_id = request_data.get("activity_id", None)
    word_num = request_data.get("word_num", None)
    if not activity_id:
        return ReturnDataApi(code=400, msg="缺少活动ID")
    if not word_num:
        return ReturnDataApi(code=400, msg="缺少工号")

    now_time = datetime.datetime.now()
    queryset_instance = all_models.InstanceComponent.objects.\
        filter(
            instance__id=activity_id,
            status=1,
            component_type=2,
            start_time__lte=now_time,
            end_time__gte=now_time,
    ).order_by("-end_time").first()
    if not queryset_instance:
        return ReturnDataApi(code=401, msg="不在活动时间内")

    queryset_user = Profile.objects.filter(username=word_num, is_active=1).first()
    if not queryset_user:
        return ReturnDataApi(code=402, msg="输入工号匹配不到员工信息")

    record_count = all_models.DiscountRecord.objects.filter(
        instance_component__id=queryset_instance.id,
        user__username=word_num
    ).count()
    if record_count >= queryset_instance.draw_num:
        if record_count == 1:
            return ReturnDataApi(code=403, msg="已参与本次抽奖，不能继续抽奖")
        else:
            return ReturnDataApi(code=403, msg="抽奖次数已达上限")

    # 获取奖品池
    queryset_prize = all_models.PrizePool.objects.filter(instance_component__id=queryset_instance.id, status=1)
    if not queryset_prize:
        return ReturnDataApi(code=405, msg="活动奖品池没有奖品")

    # 抽奖核心部分：乐观锁 + 事务
    with transaction.atomic():
        save_id = transaction.savepoint()

        try:
            # 创建抽奖记录
            queryset_record = all_models.DiscountRecord.objects.create(
                instance_component=queryset_instance,
                user=queryset_user
            )

            # 生成随机数，即为幸运码
            # 每个奖品根据中奖概率获得(0, 10000)对应的区间
            # 若幸运码在某个奖品区间内，说明中了这个奖品
            lucky_num = random.randint(0, 10000)
            end_num = 0
            is_win = 2
            return_result = {"code": 201, "msg": "没中奖", "data": {}}
            for item in queryset_prize:
                start_num = end_num + 1
                end_num = start_num + item.prob * 100 - 1
                # 原始数量
                origin_number = item.number
                origin_win_number = item.win_number

                # 中奖条件：1处于区间值中，2中奖数<奖品数
                if start_num <= lucky_num <= end_num and \
                        origin_win_number < origin_number:
                    is_win = 1
                    # 更新中奖数量，更新成功，抢得该奖品
                    # 否则，更新原始数据后再次更新，直到剩余奖品数为0
                    while True:
                        result = all_models.PrizePool.objects.filter(id=item.id, win_number=origin_win_number) \
                            .update(win_number=(origin_win_number + 1))
                        if result:
                            queryset_record.prize = item
                            queryset_record.is_win = 1
                            queryset_record.save()
                            luck_prize = {"id": item.id, "name": item.name, "description": item.description}
                            return_result = {"code": 200, "msg": "恭喜中奖", "data": luck_prize}
                            break
                        else:
                            newest_item = all_models.PrizePool.objects.filter(id=item.id).first()
                            origin_win_number = newest_item.win_number
                            if origin_win_number >= origin_number:
                                queryset_record.is_win = 2
                                queryset_record.save()
                                break
                    # 只要中奖1个奖品就跳出循环
                    break

            if is_win == 2:
                queryset_record.is_win = 2
                queryset_record.save()

        except Exception as e:
            logger_activity.error(e)
            transaction.savepoint_rollback(save_id)
            return ReturnDataApi(code=406, msg="抽奖出现异常")

    # 抽奖数据保存成功，提交事务
    transaction.savepoint_commit(save_id)
    return ReturnDataApi(**return_result)