$(document).ready(function () {
	$.getJSON(window.config.appiumAndroidDeviceList, function(appiumAndroid) {
		var tr;
		var appiumAndroidclass;
		for (var i = 0; i < appiumAndroid.length; i++) {
			if(appiumAndroid[i].DevicesStatus == 0){appiumAndroidclass = "result_offline";disabled = "disabled";}
			if(appiumAndroid[i].DevicesStatus == 1){appiumAndroidclass = "result_available";disabled = "";}
			tr = $('<tr style="border-bottom:1px solid #ddd">');
			tr.append("<td class='android-device'><input type='checkbox' name='devices_android' "+disabled+" class='android-checkbox' value="+ appiumAndroid[i].DevicesLabel +" />"+ appiumAndroid[i].DevicesLabel + "</td>");
			tr.append("<td class='android-device'> <i class='fa fa-circle "+appiumAndroidclass+"' aria-hidden='false'></i></td>");
			tr.append("<td class='android-device'>" + appiumAndroid[i].Version + "</td>");
			tr.append("<td class='android-device'>" + appiumAndroid[i].SerialNo + "</td>");
			tr.append("<td class='android-device'>" + appiumAndroid[i].Env + "</td></tr>");	
			$('#android_result').append(tr);
		}
	});
	$('#button').click(function(){
		$('#android_result').load('/ #actions', function() {
			$.getJSON(window.config.appiumAndroidDeviceList, function(appiumAndroid){
				for (var i = 0; i < appiumAndroid.length; i++) {
						if(appiumAndroid[i].DevicesStatus == 0){appiumAndroidclass = "result_offline";}
						if(appiumAndroid[i].DevicesStatus == 1){appiumAndroidclass = "result_available";}
						tr = $('<tr style="border-bottom:1px solid #ddd">');
						tr.append("<td class='android-device'><input type='checkbox' name='devices_android' "+disabled+" class='android-checkbox' value="+ appiumAndroid[i].DevicesLabel +" />"+ appiumAndroid[i].DevicesLabel + "</td>");
						tr.append("<td class='android-device'> <i class='fa fa-circle "+appiumAndroidclass+"' aria-hidden='false'></i></td>");
						tr.append("<td class='android-device'>" + appiumAndroid[i].Version + "</td>");
						tr.append("<td class='android-device'>" + appiumAndroid[i].SerialNo + "</td>");
						tr.append("<td class='android-device'>" + appiumAndroid[i].Env + "</td></tr>");
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
			if(appiumIOS[i].DevicesStatus == 0){appiumIOSclass = "result_offline";disabled = "disabled";}
			if(appiumIOS[i].DevicesStatus == 1){appiumIOSclass = "result_available";disabled = "";}
			tr = $('<tr style="border-bottom:1px solid #ddd">');
			tr.append("<td class='android-device'><input type='checkbox' name='devices_ios' "+disabled+" class='android-checkbox' value="+ appiumIOS[i].DevicesLabel +"  />"+ appiumIOS[i].DevicesLabel + "</td>");
			tr.append("<td class='android-device'> <i class='fa fa-circle "+appiumIOSclass+"' aria-hidden='false'></i></td>");
			tr.append("<td class='android-device'>" + appiumIOS[i].Version + "</td>");
			tr.append("<td class='android-device'>" + appiumIOS[i].SerialNo + "</td>");
			tr.append("<td class='android-device'>" + appiumIOS[i].Env + "</td></tr>");	
			$('#ios_result').append(tr);
		}
	});
	$('#button2').click(function(){
		$('#ios_result').load('/ #actions2', function() {
			$.getJSON(window.config.appiumIOSDeviceList, function(appiumIOS){
				for (var i = 0; i < appiumIOS.length; i++) {
						if(appiumIOS[i].DevicesStatus == 0){appiumIOSclass = "result_offline";}
						if(appiumIOS[i].DevicesStatus == 1){appiumIOSclass = "result_available";}
						tr = $('<tr style="border-bottom:1px solid #ddd">');
						tr.append("<td class='android-device'><input type='checkbox' "+disabled+" name='devices_ios' class='android-checkbox' value="+ appiumIOS[i].DevicesLabel +"  />"+ appiumIOS[i].DevicesLabel + "</td>");
						tr.append("<td class='android-device'> <i class='fa fa-circle "+appiumIOSclass+"' aria-hidden='false'></i></td>");
						tr.append("<td class='android-device'>" + appiumIOS[i].Version + "</td>");
						tr.append("<td class='android-device'>" + appiumIOS[i].SerialNo + "</td>");
						tr.append("<td class='android-device'>" + appiumIOS[i].Env + "</td></tr>");
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
	var j = $(e.target).attr("data-chk");
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
	var j = $(e.target).attr("data-chk");
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
            parentresult_android += "<a href='#' id='btn-1_android' data-target='#submenu_android"+j+"' aria-expanded='false'>";
            parentresult_android += "<input name='suites_android' value=\'"+item+"\' onclick='parentClick_android(event)' type='checkbox' class='parentCheckBox_android' data-chk="+j+"  data-count_android=\'"+j+"\' data-len-android=\'"+childItem.length+"\' /></a>";
            parentresult_android += "<a href='#testsuite-android"+j+"' data-toggle='tab' onclick='navClick_android(event)'>"+item+"</a></label></li><hr>";
            $("#testsuite-android ul").append(parentresult_android);
            if(j==0) {
				active='active';
            }
            childresult_android ="<div class='tab-pane "+active+" view_chk_android"+j+" ' id='testsuite-android"+j+"'><ul class='nav' id='submenu_android"+j+"' role='menu' aria-labelledby='btn-1_android'>";
            $.each(childItem, function(child,val){
				childresult_android += "<li><label class='checkbox' for='one' class='revo_dropdown'><input type='checkbox' class='childCheckBox_android chk_android"+j+"' name='cases_android' value=\'"+val+"\'  />"+val+"</label></li><hr>";
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
            parentresult_ios = "<li ><label class='checkbox "+active+" revo_dropdown' name='suites_ios'  for='two' >";
            parentresult_ios += "<a href='#' id='btn-1_ios' data-target='#submenu_ios"+j+"' aria-expanded='false'>";
            parentresult_ios += "<input name='suites_ios' value=\'"+item+"\' onclick='parentClick_ios(event)' type='checkbox' class='parentCheckBox_ios' data-chk="+j+"  data-count_ios=\'"+j+"\' data-len-ios=\'"+childItem.length+"\' /></a>";
            parentresult_ios += "<a href='#testsuite-ios"+j+"' data-toggle='tab' onclick='navClick_ios(event)'>"+item+"</a></label></li><hr>";
            $("#testsuite-ios ul").append(parentresult_ios);
            if(j==0) {
				active='active';
            }
            childresult_ios ="<div class='tab-pane_ios "+active+" view_chk_ios"+j+" ' id='testsuite-ios"+j+"'><ul class='nav' id='submenu_ios"+j+"' role='menu' aria-labelledby='btn-1_ios'>";
            $.each(childItem, function(child,val){
				childresult_ios += "<li><label class='checkbox' for='two' class='revo_dropdown'><input type='checkbox' class='childCheckBox_ios chk_ios"+j+"' name='cases_ios' value=\'"+val+"\'  />"+val+"</label></li><hr>";
				i++;
            });
            childresult_ios +="</ul></div>";
            j++;
            $("#testcase-ios").append(childresult_ios);
        });    
	});
}

$.fn.serializeObject = function() {
	var runAppiumJson = {};
    runAppiumJson['devices_android']=[];
	runAppiumJson['devices_ios']=[];
    runAppiumJson['suites_android']=[];
	runAppiumJson['suites_ios']=[];
    var count=0;
    var o = {};
    var a = this.serializeArray();
    var schedule = [];
    var suite_android = [];
	 var suite_ios = [];
    var casesarry_android = [];
	var casesarry_ios = [];
	
    $.each(a, function(key,values) {
		
		if(values.name=='devices_android'){        
			var x_android=values.value;
			suite_android.push(x_android);
		}
		if(values.name=='devices_ios'){        
			var x_ios=values.value;
			suite_ios.push(x_ios);
		}
		if(values.name=='cases_android'){
			casesarry_android.push(values.value);
		} 
		if(values.name=='cases_ios'){
			casesarry_ios.push(values.value);
		}         
		if(values.name=='suites_android'){
			runAppiumJson['suites_android'].push({'name':values.value,'cases_android':null});
			count++;
		}
		if(values.name=='suites_ios'){
			runAppiumJson['suites_ios'].push({'name':values.value,'cases_ios':null});
			count++;
		}
    });
   
   runAppiumJson['devices_android'] = suite_android;
	runAppiumJson['devices_ios'] = suite_ios;
	var all_android=0, all_ios=0, count=0, count_ios=0;
    $('.parentCheckBox_android:checked').each(function(){
		var len=$(this).attr('data-len-android');
		var arrycases_android=[];		
		len=parseInt(len)+ parseInt(all_android);
        for(var i=all_android; i<len; i++) {
			arrycases_android.push(casesarry_android[i]);
		}		
		all_android=parseInt(arrycases_android.length)+parseInt(all_android);
		runAppiumJson['suites_android'][count].cases_android=arrycases_android;
		count++;
    });
	$('.parentCheckBox_ios:checked').each(function(){
		len=$(this).attr('data-len-ios');
		var arrycases_ios=[];
		len=parseInt(len)+ parseInt(all_ios);
        for(var i=all_ios; i<len; i++) {
			arrycases_ios.push(casesarry_ios[i]);
		}
		all_ios=parseInt(arrycases_ios.length)+parseInt(all_ios);
		runAppiumJson['suites_ios'][count_ios].cases_ios=arrycases_ios;
		count_ios++;
    });
	window.runAppiumJson = runAppiumJson;
	
}


function runJobForm() {
	$('#run-job').submit(function() {
		event.preventDefault();
		$('form').serializeObject();
		$.ajax({
			type: "POST",
			url: window.config.appium_run,
			data: JSON.stringify(window.runAppiumJson),
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
	var allOpts = $('#lstBox1 option');
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
			$('#lstBox1 option[value="' + opt.value + '"]').prop('selected', true)
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
			$('#lstBox1 option[value="' + opt.value + '"]').prop('selected', true )
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
			$('#lstBox1 option[value="' + opt.value + '"]').prop('selected', false)
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
			$('#lstBox1 option[value="' + opt.value + '"]').prop('selected', false)
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

