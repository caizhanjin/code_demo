# 文件的上传下载

## 下载文件
服务端：
``` 
@csrf_exempt
def get_vertical_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f"attachment; filename={filename}"

    response.write(codecs.BOM_UTF8)
    writer = csv.writer(response)
    writer.writerow(header)
    writer.writerows(result)

    print(f"总耗时{start_time}")
    return response
```
客户端：
``` 
download(){
    var file_name = "test.csv"
    var ajax = new XMLHttpRequest();
    ajax.open("POST", this.$path + "report/get_vertical_csv/", true);
    ajax.responseType = 'blob';
    ajax.onload = function (e) {
        var eleLink = document.createElement('a');
        eleLink.download = file_name;
        eleLink.style.display = 'none';
        var blob = new Blob([e.target.response]);
        eleLink.href = URL.createObjectURL(blob);
        document.body.appendChild(eleLink);
        eleLink.click();
        document.body.removeChild(eleLink);
    }
    setTimeout(function () { ajax.send() }, 0)
},
```

## 上传文件

服务端：
``` 
def upload_attach(request):
    """上传附件"""
    attach_data = request.FILES.get('attach')
    attach_name = request.POST.get('attach_name')
    try:
        with open(save_file, 'wb') as f:
            for chunk in attach_data.chunks():
                f.write(chunk)
    except Exception as error:
        return ReturnDataApi(code=400, msg='附件上传失败' + error.args[0])

    return ReturnDataApi()
```
客户端：
``` 
<input type="file" name="photo" id="file_id" @change="changeImg">
<input type="file" name="photo" id="file_id2" style="display:none">

resetFileInput(){
    this.files_data = ""
    this.file_name = ""
    var file = document.getElementById('file_id')
    
    file.value = null
    file.files = document.getElementById('file_id2').files
},
changeImg(e){
    const input = e.target;
    const files = e.target.files;
    if(files && files[0]) {
        const file = files[0];
        this.files_data = file
    }
},

uploadAttach(){
    if(this.is_upload_ing==true){ return }
    if(this.files_data==""){
        this.$message({type: "info", message: "请选择文件"});
        return
    }

    var formdata = new FormData()
    formdata.append('attach', this.files_data)
    formdata.append('attach_name', this.file_name)
    
    const instance = this.$axios.create()
    this.is_upload_ing = true
    instance({
        url: this.$path + "event/upload_attach/",
        method: 'post',
        data: formdata,
        headers: { 'Content-Type': 'multipart/form-data' },
    }).then((res) => {
        this.is_upload_ing = false
        if(res.data.code==200){
            this.form_data.attach_list.push(res.data.data)
            this.resetFileInput()
            this.$forceUpdate()
        }else{
            this.$message({type: "error", message: this.$t('tips.fail') + ":" + res.data.msg});
        }
    })
},
```
