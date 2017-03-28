$(document).ready(function () {

	$("#android_version").change(function () {
		
		var val = $(this).val();
		
		$(".device-box").css("display", "block");
		$("#ios").removeClass('in');
		$("#android").addClass('in');
		$("#ios").removeClass('in');
		if (val == "") {
			$("#android").removeClass('in');
			
		}
		if (val == "Version1") {
			$("#android").html("<p><input type=checkbox name=chk >&nbsp;Android Device1</p><p><input type=checkbox name=chk >&nbsp;Android Device2</p>");
			
		} else if (val == "Version2") {
			$("#android").html("<p><input type=checkbox name=chk >&nbsp;Android Device3</p><p><input type=checkbox name=chk >&nbsp;Android Device4</p>");
		} else if (val == "Version3") {
			$("#android").html("<p><input type=checkbox name=chk >&nbsp;Android Device5</p><p><input type=checkbox name=chk >&nbsp;Android Device6</p>");
		}
	});
		
	$("#ios_version").change(function () {

		var val = $(this).val();
		$("#android").removeClass('in');
		$("#ios").addClass('in');
		if (val == "") {
			$("#ios").removeClass('in');
		
		}
		if (val == "IOSVersion1") {
			$("#ios").html("<p><input type=checkbox name=chk >&nbsp;IOS Device1</p><p><input type=checkbox name=chk >&nbsp;IOS Device2</p>");
			
		} else if (val == "IOSVersion2") {
			$("#ios").html("<p><input type=checkbox name=chk >&nbsp;IOS Device3</p><p><input type=checkbox name=chk >&nbsp;IOS Device4</p>");
		} else if (val == "IOSVersion3") {
			$("#ios").html("<p><input type=checkbox name=chk >&nbsp;IOS Device5</p><p><input type=checkbox name=chk >&nbsp;IOS Device6</p>");
		}
	});
});

$(document).ready(function () {
	$.getJSON(window.config.appiumAndroidDeviceList, function(appiumAndroid) {
		var tr;
		var appiumAndroidclass;
		for (var i = 0; i < appiumAndroid.length; i++) {
			if(appiumAndroid[i].DevicesStatus == 0){appiumAndroidclass = "result_offline";}
			if(appiumAndroid[i].DevicesStatus == 1){appiumAndroidclass = "result_available";}
			tr = $('<tr/>');
			tr.append("<td style='padding:5px; width:100px;text-align:center;font-size:12px'><input type='checkbox' name='chk[]' style='margin-right:5px;margin-left:5px' />"+ appiumAndroid[i].DevicesLabel + "</td>");
			tr.append("<td style='padding:5px; width:100px; text-align:center;font-size:12px'> <i class='fa fa-circle "+appiumAndroidclass+"' aria-hidden='false'></i></td>");
			tr.append("<td style='padding:5px; width:100px; text-align:center;font-size:12px'>" + appiumAndroid[i].Version + "</td>");
			tr.append("<td style='padding:5px; width:100px; text-align:center;font-size:12px'>" + appiumAndroid[i].SerialNo + "</td>");
			tr.append("<td style='padding:5px; width:100px; text-align:center;font-size:12px'>" + appiumAndroid[i].Env + "</td>");	
			$('#android_result').append(tr);
		}
	});
	$('#button').click(function(){
		$('#android_result').load('/ #actions', function() {
			$.getJSON(window.config.appiumAndroidDeviceList, function(appiumAndroid){
				for (var i = 0; i < appiumAndroid.length; i++) {
						if(appiumAndroid[i].DevicesStatus == 0){appiumAndroidclass = "result_offline";}
						if(appiumAndroid[i].DevicesStatus == 1){appiumAndroidclass = "result_available";}
						tr = $('<tr/>');
						tr.append("<td style='padding:5px; width:100px;text-align:center;font-size:12px'><input type='checkbox' name='chk[]' style='margin-right:5px;margin-left:5px' />"+ appiumAndroid[i].DevicesLabel + "</td>");
						tr.append("<td style='padding:5px; width:100px; text-align:center;font-size:12px'> <i class='fa fa-circle "+appiumAndroidclass+"' aria-hidden='false'></i></td>");
						tr.append("<td style='padding:5px; width:100px; text-align:center;font-size:12px'>" + appiumAndroid[i].Version + "</td>");
						tr.append("<td style='padding:5px; width:100px; text-align:center;font-size:12px'>" + appiumAndroid[i].SerialNo + "</td>");
						tr.append("<td style='padding:5px; width:100px; text-align:center;font-size:12px'>" + appiumAndroid[i].Env + "</td>");
						$('#android_result').append(tr);
				}
			});
		});
	}); 
});

$(document).ready(function () {
	$.getJSON(window.config.appiumIOSDeviceList, function(appiumIOS) {
		var tr;
		var appiumIOSclass;
		for (var i = 0; i < appiumIOS.length; i++) {
			if(appiumIOS[i].DevicesStatus == 0){appiumIOSclass = "result_offline";}
			if(appiumIOS[i].DevicesStatus == 1){appiumIOSclass = "result_available";}
			tr = $('<tr/>');
			tr.append("<td style='padding:5px; width:100px;text-align:center;font-size:12px'><input type='checkbox' name='chk[]' style='margin-right:5px;margin-left:5px' />"+ appiumIOS[i].DevicesLabel + "</td>");
			tr.append("<td style='padding:5px; width:100px; text-align:center;font-size:12px'> <i class='fa fa-circle "+appiumIOSclass+"' aria-hidden='false'></i></td>");
			tr.append("<td style='padding:5px; width:100px; text-align:center;font-size:12px'>" + appiumIOS[i].Version + "</td>");
			tr.append("<td style='padding:5px; width:100px; text-align:center;font-size:12px'>" + appiumIOS[i].SerialNo + "</td>");
			tr.append("<td style='padding:5px; width:100px; text-align:center;font-size:12px'>" + appiumIOS[i].Env + "</td>");	
			$('#ios_result').append(tr);
		}
	});
	$('#button2').click(function(){
		$('#ios_result').load('/ #actions2', function() {
			$.getJSON(window.config.appiumIOSDeviceList, function(appiumIOS){
				for (var i = 0; i < appiumIOS.length; i++) {
						if(appiumIOS[i].DevicesStatus == 0){appiumIOSclass = "result_offline";}
						if(appiumIOS[i].DevicesStatus == 1){appiumIOSclass = "result_available";}
						tr = $('<tr/>');
						tr.append("<td style='padding:5px; width:100px;text-align:center;font-size:12px'><input type='checkbox' name='chk[]' style='margin-right:5px;margin-left:5px' />"+ appiumIOS[i].DevicesLabel + "</td>");
						tr.append("<td style='padding:5px; width:100px; text-align:center;font-size:12px'> <i class='fa fa-circle "+appiumIOSclass+"' aria-hidden='false'></i></td>");
						tr.append("<td style='padding:5px; width:100px; text-align:center;font-size:12px'>" + appiumIOS[i].Version + "</td>");
						tr.append("<td style='padding:5px; width:100px; text-align:center;font-size:12px'>" + appiumIOS[i].SerialNo + "</td>");
						tr.append("<td style='padding:5px; width:100px; text-align:center;font-size:12px'>" + appiumIOS[i].Env + "</td>");
						$('#ios_result').append(tr);
				}
			});
		});
	}); 
});

$(window).resize(function() {
	$(".resize_table").removeClass('fixed_head');
	$(".resize_tbody").removeClass('stb_tbody');
	setTimeout( function(){
		var count1=0;
		$(".resize_table").find('tr>th').each(function( event ) {        
			var style = window.getComputedStyle(this, null).width;
			$(".resize_tbody").find('tr>td:eq('+count1+')').attr('width',style);
			$(".resize_table").find('tr>th:eq('+count1+')').attr('width',style) ;     	  
		    count1++;
		});
		var wid = $("#stb-table").outerWidth();
		$("#example").css('width',wid+'px');
		$(".resize_table").addClass('fixed_head');
		$(".resize_tbody").addClass('stb_tbody');
   },500);  
});

$(function() {
  populateTestSuite();
  populateIOSTestSuite();
  runJobForm();
  handleTestSuiteCases();
});

//Utility Functionality added to Array
Array.prototype.contains = function(element){
	return this.indexOf(element) > -1;
};

Array.prototype.remove = function(elem, all) {
	for (var i=this.length-1; i>=0; i--) {
		if (this[i] === elem) {
			this.splice(i, 1);
			if(!all)
			break;
		}
	}
	return this;
};

function getCookie(name) {
	var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function showConsole(job_name, build_num, suite_name) {
	var title = "JOB: " + job_name +",    SUITE NAME:  " + suite_name;
	$.ajax({
		url: window.config.buildConsole ,
		type: "get",
		data:{"job": job_name, "build" : build_num },
		cache: false,
		success: function(data){
			$('#appium-modal-content').text(data);
			$('#title').text(title);
			$('#myModal').modal();
		}
	});
}

/****Select All Checkbox****/
function checkAll(ele) {
    var checkboxes = document.getElementsByName('check2');
    if (ele.checked) {
        for (var i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].type == 'checkbox' && checkboxes[i].disabled == '') {
				checkboxes[i].checked = true;
             }
         }
    }
	else {
        for (var i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].type == 'checkbox') {
				checkboxes[i].checked = false;
            }
        }
    }
}
 
function showMe (box) {
	var chboxs = document.getElementsByName("schedule");
  	var visible_value = "none";
  	for(var i=0;i<chboxs.length;i++) { 
		if(chboxs[i].checked){
			visible_value = "block";
  			break;
  		}
  	}
	document.getElementById(box).style.display = visible_value;
}

function disable_edit() {
	var obj;
	var count=0;
	var Change = document.getElementsByName('Edit_Button')[0];
	for (var i=0; i<tform.elements.length; i++) {
		obj = tform.elements[i];
		if (obj.type == "checkbox" && obj.checked) {
			count++;
		}
	}
	if(count==1){
		Change.disabled=false;
	}
	if(count>1){
		Change.disabled=true;
	}
}

function disable_edit_test(elementName, checkboxPath) {
	var changeBtn = document.getElementsByName(elementName)[0];
	if($( checkboxPath + " :checkbox:checked").length == 1) {
		changeBtn.disabled=false;
	} 
	else {
		changeBtn.disabled=true;
	}
}

function editTestCase() {
	window.location.href = $( ".list_table tr td :checkbox:checked").attr("data-edit");
	return false;
}

function parentClick_android(e){		
	$(".tab-pane").removeClass('active');
	var j = $(e.target).attr("data-chk_android");
	if($(e.target).is(":checked")){
		$('.chk_android'+j).prop('checked',true);
		$(e.target).parent().parent().addClass('selectCheckbox_android');
    }
	else{
		$('.chk_android'+j).prop('checked',false);
		$(e.target).parent().parent().removeClass('selectCheckbox_android');
	}
	$('.view_chk_android'+j).addClass('active');
}
function parentClick_ios(e){		
	$(".tab-pane_ios").removeClass('active');
	var j = $(e.target).attr("data-chk_ios");
	if($(e.target).is(":checked")){
		$('.chk_ios'+j).prop('checked',true);
		$(e.target).parent().parent().addClass('selectCheckbox_ios');
    }
	else{
		$('.chk_ios'+j).prop('checked',false);
		$(e.target).parent().parent().removeClass('selectCheckbox_ios');
	}
	$('.view_chk_ios'+j).addClass('active');
}

function navClick_android(e){
	$('.nav-tabs a').parent().removeClass('selectCheckbox_andriod');
	$(e.target).parent().addClass('selectCheckbox_andriod');
}
function navClick_ios(e){
	$('.nav-tabs a').parent().removeClass('selectCheckbox_ios');
	$(e.target).parent().addClass('selectCheckbox_ios');
}
/*android test suite & test case*/
function populateTestSuite() {
	$.getJSON(window.config.appiumAndroidTestSuiteWithCases, function(result) {
		var parentresult_android, childresult_android,i = 0,j=0;
        $.each(result,function(item,childItem){
			var active='';
            if(j==0) {
				active='selectCheckbox_andriod';
            }
            parentresult_android = "";
            parentresult_android = "<li ><label class='checkbox "+active+" revo_dropdown' name='suites_android'  for='one' >";
            parentresult_android += "<a href='#' id='btn-1' data-target='#submenu_android"+j+"' aria-expanded='false'>";
            parentresult_android += "<input name='suites_android' value=\'"+item+"\' onclick='parentClick_android(event)' type='checkbox' class='parentCheckBox_android' data-chk_android="+j+"  data-count=\'"+j+"\' data-len=\'"+childItem.length+"\' /></a>";
            parentresult_android += "<a href='#testsuite-android"+j+"' data-toggle='tab' onclick='navClick_android(event)'>"+item+"</a></label></li><hr>";
            $("#testsuite-android ul").append(parentresult_android);
            if(j==0) {
				active='active';
            }
            childresult_android ="<div class='tab-pane "+active+" view_chk_android"+j+" ' id='testsuite-android"+j+"'><ul class='nav' id='submenu_android"+j+"' role='menu' aria-labelledby='btn-1'>";
            $.each(childItem, function(child,val){
				childresult_android += "<li><label class='checkbox' for='one' class='revo_dropdown'><input type='checkbox' class='childCheckBox_android chk_android"+j+"' name='cases' value=\'"+val+"\'  />"+val+"</label></li><hr>";
				i++;
            });
            childresult_android +="</ul></div>";
            j++;
            $("#testcase-android").append(childresult_android);
        });    
	});
}

/*ios test suite & test case*/
function populateIOSTestSuite() {
	$.getJSON(window.config.appiumIOSTestSuiteWithCases, function(result) {
		var parentresult_ios, childresult_ios,i = 0,j=0;
        $.each(result,function(item,childItem){
			var active='';
            if(j==0) {
				active='selectCheckbox_ios';
            }
            parentresult_ios = "";
            parentresult_ios = "<li ><label class='checkbox "+active+" revo_dropdown' name='suites_ios'  for='one' >";
            parentresult_ios += "<a href='#' id='btn-1' data-target='#submenu_ios"+j+"' aria-expanded='false'>";
            parentresult_ios += "<input name='suites_ios' value=\'"+item+"\' onclick='parentClick_ios(event)' type='checkbox' class='parentCheckBox_ios' data-chk_ios="+j+"  data-count=\'"+j+"\' data-len=\'"+childItem.length+"\' /></a>";
            parentresult_ios += "<a href='#testsuite-ios"+j+"' data-toggle='tab' onclick='navClick_ios(event)'>"+item+"</a></label></li><hr>";
            $("#testsuite-ios ul").append(parentresult_ios);
            if(j==0) {
				active='active';
            }
            childresult_ios ="<div class='tab-pane_ios "+active+" view_chk_ios"+j+" ' id='testsuite-ios"+j+"'><ul class='nav' id='submenu_ios"+j+"' role='menu' aria-labelledby='btn-1'>";
            $.each(childItem, function(child,val){
				childresult_ios += "<li><label class='checkbox' for='one' class='revo_dropdown'><input type='checkbox' class='childCheckBox_ios chk_ios"+j+"' name='cases' value=\'"+val+"\'  />"+val+"</label></li><hr>";
				i++;
            });
            childresult_ios +="</ul></div>";
            j++;
            $("#testcase-ios").append(childresult_ios);
        });    
	});
}

$.fn.serializeObject = function() {
	var runRevoJson = {};
    runRevoJson['scheduled']= 'false';
    runRevoJson['time']='';
    runRevoJson['stbs']=[];
    runRevoJson['suites']=[];
    var count=0;
    var o = {};
    var a = this.serializeArray();
    var schedule = [];
    var suite = [];
    var casesarry = [];
    $.each(a, function(key,values) {
		if(values.name=='schedule'){
			runRevoJson['scheduled'] = values.value;
		}  	
		if(values.name=='time'){
			runRevoJson['time'] = values.value;
		}        
		if(values.name=='stbs'){        
			var x=values.value;
			suite.push(x);
		}
		if(values.name=='cases'){
			casesarry.push(values.value);
		}         
		if(values.name=='suites'){
			runRevoJson['suites'].push({'name':values.value,'cases':null});
			count++;
		}
    });
    runRevoJson['stbs'] = suite;
	var all=0, count=0;
    $('.parentCheckBox:checked').each(function(){
		var len=$(this).attr('data-len');
		var arrycases=[];
		len=parseInt(len)+ parseInt(all);
        for(var i=all; i<len; i++) {
			arrycases.push(casesarry[i]);
		}
		all=parseInt(arrycases.length)+parseInt(all);
		runRevoJson['suites'][count].cases=arrycases;
		count++;
    });
	window.runRevoJson = runRevoJson;
}

function runJobForm() {
	$('#run-job').submit(function() {
		event.preventDefault();
		$('form').serializeObject();
		$.ajax({
			type: "POST",
			url: window.config.revo_run,
			data: JSON.stringify(window.runRevoJson),
			headers: { "X-CSRFToken":  getCookie('csrftoken') },
			success: function(response) {
			},
			dataType: "json",
			contentType : "application/json"
		});
		window.location.href = window.config.appium;
		return false;
	});
}

function handleTestSuiteCases() {
	var allOpts = $('#lstBoxMain option');
	$('#lstBox1').append($(allOpts).clone());
	var selectedOpts = $('#lstBox1 option:selected');
	$('#lstBox2').append($(selectedOpts).clone());
	$(selectedOpts).remove();
	$('#btnRight').click(function (e) {
		var selectedOpts = $('#lstBox1 option:selected');
		if (selectedOpts.length == 0) {
			alert("Nothing to move.");
			e.preventDefault();
		}
		$('#lstBox2').append($(selectedOpts).clone());
		$(selectedOpts).remove();
		selectedOpts.each(function(key,opt) {
			$('#lstBoxMain option[value="' + opt.value + '"]').prop('selected', true)
		});
		e.preventDefault();
	});
	$('#btnAllRight').click(function (e) {
		var selectedOpts = $('#lstBox1 option');
		if (selectedOpts.length == 0) {
			alert("Nothing to move.");
			e.preventDefault();
		}
		$('#lstBox2').append($(selectedOpts).clone());
		$(selectedOpts).remove();
		selectedOpts.each(function(key,opt) {
			$('#lstBoxMain option[value="' + opt.value + '"]').prop('selected', true )
		});
		e.preventDefault();
	});
	$('#btnLeft').click(function (e) {
		var selectedOpts = $('#lstBox2 option:selected');
		if (selectedOpts.length == 0) {
			alert("Nothing to move.");
			e.preventDefault();
		}
		$('#lstBox1').append($(selectedOpts).clone());
		$(selectedOpts).remove();
		selectedOpts.each(function(key,opt) {
			$('#lstBoxMain option[value="' + opt.value + '"]').prop('selected', false)
		});
		e.preventDefault();
	});
	$('#btnAllLeft').click(function (e) {
		var selectedOpts = $('#lstBox2 option');
		if (selectedOpts.length == 0) {
			alert("Nothing to move.");
			e.preventDefault();
		}
		$('#lstBox1').append($(selectedOpts).clone());
		$(selectedOpts).remove();
		selectedOpts.each(function(key,opt) {
			$('#lstBoxMain option[value="' + opt.value + '"]').prop('selected', false)
		});
		e.preventDefault();
	});
}
				
function stb_table(){			
   var count=0;
   var td_array = [];
   $(".fixed_head").find('tr>th').each(function( event ) {
		var thWdith = window.getComputedStyle(this, null).width;
		td_array.push(thWdith);
		$(".resize_table").find('tr>th:eq('+count+')').attr('width',thWdith);
		count++;
   });
   return td_array;
}

