$( document ).ready(function() {
  var base_color = "rgb(230,230,230)";
  var active_color = "rgb(237, 40, 70)";
  var inp=[];
  
  
  var child = 1;
  var length = $("section").length - 1;
  $("#prev").addClass("disabled");
  $("#submit").addClass("disabled");
  $('.button1').hide();
  
  $("section").not("section:nth-of-type(1)").hide();
  $("section").not("section:nth-of-type(1)").css('transform','translateX(100px)');
  
  var svgWidth = length * 200 + 24;
  $("#svg_wrap").html(
    '<svg version="1.1" id="svg_form_time" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 ' +
      svgWidth +
      ' 24" xml:space="preserve"></svg>'
  );
  
  function makeSVG(tag, attrs) {
    var el = document.createElementNS("http://www.w3.org/2000/svg", tag);
    for (var k in attrs) el.setAttribute(k, attrs[k]);
    return el;
  }
  
  for (i = 0; i < length; i++) {
    var positionX = 12 + i * 200;
    var rect = makeSVG("rect", { x: positionX, y: 9, width: 200, height: 6 });
    document.getElementById("svg_form_time").appendChild(rect);
    // <g><rect x="12" y="9" width="200" height="6"></rect></g>'
    var circle = makeSVG("circle", {
      cx: positionX,
      cy: 12,
      r: 12,
      width: positionX,
      height: 6
    });
    document.getElementById("svg_form_time").appendChild(circle);
  }
  
  var circle = makeSVG("circle", {
    cx: positionX + 200,
    cy: 12,
    r: 12,
    width: positionX,
    height: 6
  });
  document.getElementById("svg_form_time").appendChild(circle);
  
  $('#svg_form_time rect').css('fill',base_color);
  $('#svg_form_time circle').css('fill',base_color);
  $("circle:nth-of-type(1)").css("fill", active_color);
  
   
  $(".button").click(function () {
    $("#svg_form_time rect").css("fill", active_color);
    $("#svg_form_time circle").css("fill", active_color);
    var id = $(this).attr("id");
    if (id == "next") {
      if($('#nofnqueen').val()!=undefined && $('#nofnqueen').val()<=10 && $('#nofnqueen').val()>=4){
        $("#prev").removeClass("disabled");
        $('.button1').show();
        $('.button1').html('Wanna Try?');
        if (child >= length) {
          $(this).addClass("disabled");
          $('#submit').removeClass("disabled");
        }
        if (child <= length) {
          child++;
        }
      }
      else{
        alert('Please provide a value between 4 and 10');
      }
    } else if (id == "prev") {
      inp=[];
      s=0;
      $('#chessboard').empty();
      $('.button1').hide();
      $("#next").removeClass("disabled");
      $('#submit').addClass("disabled");
      if (child <= 2) {
        $(this).addClass("disabled");
      }
      if (child > 1) {
        child--;
      }
    }


    var circle_child = child + 1;
    $("#svg_form_time rect:nth-of-type(n + " + child + ")").css(
      "fill",
      base_color
    );
    $("#svg_form_time circle:nth-of-type(n + " + circle_child + ")").css(
      "fill",
      base_color
    );
    var currentSection = $("section:nth-of-type(" + child + ")");
    currentSection.fadeIn();
    currentSection.css('transform','translateX(0)');
   currentSection.prevAll('section').css('transform','translateX(-100px)');
    currentSection.nextAll('section').css('transform','translateX(100px)');
    $('section').not(currentSection).hide();
  });
  var s=0;
  $(".button1").click(function () {
    if(s==0){
      $(".button1").html("Let computer decide");
      $('#population').hide();
      var n=$('#nofnqueen').val();
      for(var i=0;i<n;i++){
        inp.push(-1);
        $('#chessboard').append(`<tr id='`+ i +`'>`);
        for(var j=0;j<n;j++){
          if(((i+j)%2)==0)
            $('#'+i.toString()).append(`<td class="chessboard even" id="`+ i+j +`"></td>`);
          else
            $('#'+i.toString()).append(`<td class="chessboard odd" id="`+ i+j +`"></td>`);
        }
        $('#chessboard').append(`</tr>`);
      }
      if(n>8){
        $('td').css('height','6vh');
        $('td').css('width','6vh');
      }
      else if(n>7){
        $('td').css('height','8vh');
        $('td').css('width','8vh');
      }
      else if(n>4){
        $('td').css('height','10vh');
        $('td').css('width','10vh');
      }
      else{
        $('td').css('height','14vh');
        $('td').css('width','14vh');
      }
      s=1;
    }
    else{
      inp=[];
      $('.button1').html('Wanna Try?');
      $('#chessboard').empty();
      $('#population').show();
      s=0;
    }
  });
  $("#chessboard").on("click", "td", function() {
    for(var i=0;i<inp.length;i++){
      for(var j=0;j<inp.length;j++){
        if((i+j)%2==0){
          $('#'+i.toString()+j.toString()).css({"background-color":"#441a03"});
        }
        else{
          $('#'+i.toString()+j.toString()).css({"background-color":"#8b6d43"});
        }
      }
    }
    
    var strnum=$(this).attr('id');
    var num=parseInt($(this).attr('id'));
    var row=parseInt(num/10);
    var column=num%10;
    var bslash={},fslash={};
    if(!$(this).is(':empty')){
      $(this).empty();
      inp[row]=-1
    }
    else{
      for(var i=0;i<inp.length;i++){
        if(inp[i]==column){
          $('#'+i.toString()+inp[i].toString()).empty();
          
          inp[i]=-1;
        }
      }
      if(inp[row]!=-1)
        $('#'+row.toString()+inp[row].toString()).empty();
      inp[row]=column;
      $('#'+strnum.toString()).append('♛');
    }
    for(var i=0;i<inp.length;i++){
      if(inp[i]!=-1){
        if(i+inp[i] in fslash){
          var que=fslash[i+inp[i]];
          $('#'+que[0].toString()+que[1].toString()).css({"background-color":"red"})
          $('#'+i.toString()+inp[i].toString()).css({"background-color":"red"});
        }
        else{
          fslash[i+inp[i]]=[i,inp[i]];
        }
        if(i-inp[i] in bslash){
          var que=bslash[i-inp[i]];
          $('#'+que[0].toString()+que[1].toString()).css({"background-color":"red"})
          $('#'+i.toString()+inp[i].toString()).css({"background-color":"red"});
        }
        else{
          bslash[i-inp[i]]=[i,inp[i]];
        }
      }
    }
    // alert(bslash.filter((item, index) => bslash.indexOf(item) !== index));
    // alert(fslash.filter((item, index) => fslash.indexOf(item) !== index));
  });

  submitForm = function () {

    //to be commented
    var flag=0;
    var ans='';
    let n = $('#nofnqueen').val();
    if(s==0){
      let p = $('#pofnqueen').val();
      //
      if (p < 2) {
          alert("Please enter Intial Population Size >2 !");
          flag=1;
      }
    }
    else{
      var count=0;
      for(var i=0;i<inp.length;i++){
        ans+=inp[i].toString();
        if(inp[i]==-1){
          count+=1;
        }
      }
      if(count==inp.length){
        alert('Provide atleast 1 input');
        flag=1;
      }
    }

    if(flag==0){
      $('#formn').val($('#nofnqueen').val());
      if(s==0)
        $('#formp').val($('#pofnqueen').val().toString());
      else
        $('#formp').val(inp);
      $('#npform').submit();
    }
    else{
      if(s=1){
        $('.button1').click();
      }
    }
}
  });