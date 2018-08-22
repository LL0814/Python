$("#submit").click(function () {
    var isComplated = true;
    var a1,a2,a3,a7,a8,a9,a10;
    var a4 = '/';
    var a5 = '/';
    var a6 = '/';
   for(var i = 1 ; i <= 10 ; i++)
    {
        var thisId = 'Q' + i.toString();
        $("#"+thisId).find("input").each(function(){
            if(i == 1)
            {
                if(this.checked)
                {
                    a1 = this.id;
                }
                else{
                    isComplated =false
                }
            }
            else if(i == 2)
            {
                if(this.checked)
                {
                    a2 = this.id;
                }
                else{
                    isComplated =false
                }
            }
            else if(i == 3)
            {
                if(this.value == undefined && this.value==null)
                {
                    a3 = this.value;
                }
                else{
                    isComplated =false
                }
            }
            else if(i == 4)
            {
                if(this.checked)
                {
                    a4 += this.id + '/';
                }
                else{
                    isComplated =false
                }
            }
            else if(i == 5)
            {
                if(this.checked)
                {
                    a5 += this.id + '/';
                }
                else{
                    isComplated =false
                }
            }
            else if(i == 6)
            {
                if(this.value != undefined && this.value !=null)
                {
                    a6 += this.value + '/';
                }
                else{
                    isComplated =false
                }
            }
            else if(i == 7)
            {
                if(this.checked)
                {
                    a7 = this.id;
                }
                else{
                    isComplated =false
                }
            }
            else if(i == 8)
            {
                if(this.checked)
                {
                    a8 = this.id;
                }
                else{
                    isComplated =false
                }
            }
            else if(i == 9)
            {
                if(this.checked)
                {
                    a9 = this.id;
                }
                else{
                    isComplated =false
                }
            }
            else if(i == 10)
            {
                if(this.checked)
                {
                    a10 = this.id;
                }
                else{
                    isComplated =false
                }
            }
        })
    }
    var data = {
        'a1': a1,
        'a2': a2,
        'a3': a3,
        'a4': a4,
        'a5': a5,
        'a6': a6,
        'a7': a7,
        'a8': a8,
        'a9': a9,
        'a10': a10,
    }
    if(isComplated)
    {
        ajax(data, '/survey/');
        window.location.href = '/thanks/';
    }
    else{
        alert("请完成该问卷全部题目，谢谢");
    }
});

function ajax(formData, URL){
    $.ajax({
        type:'POST',
        url: URL,
        data: JSON.stringify(formData),//必要
        dataType:"json",
        contentType:"application/json",
        headers: {
            'X-CSRFToken': $.cookie('csrftoken')
        },
        processData: false,
        contentType: false,
        async: true,
        success: function(data) {
        }
    });
}