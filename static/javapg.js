$(document).ready(function(){
    $.ajax({
        method: "GET",
        url: "http://localhost:8000/api/countries/",
        success: function(countries){
            $.each(countries, function(){
                
                $("#country").append("<option value='" + this.code + "'>"+ this.name + "</option>");
            });
        }
    });
    
    $("#country").change(function(){
        $("#states").empty();  
        $.ajax({
            type: "POST",
            url: "http://localhost:8000/api/states/",
            data: {"country": $("#country").val()},
            success: function(states) {
                $.each(states, function(){
                
                    $("#states").append("<option value='" + this.code + "'>" + this.name + "</option>")
                
                    var options = $('#states option');
                    var arr = options.map(function(a, element) { return { t: $(element).text(), v: element.value }; }).get();
                    arr.sort(function(item1, item2) { return item1.t > item2.t ? 1 : item1.t < item2.t ? -1 : 0; });
                    options.each(function(i, e)  {
                        e.value = arr[i].v;
                        $(e).text(arr[i].t);
                    });

                });
            }   
        });
        
    });
    
});