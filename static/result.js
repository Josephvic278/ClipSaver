document.addEventListener('DOMContentLoaded', function() {
    var vid_value = document.getElementById("res_input")
    var res_con_ = document.getElementById("vid_value")
    res_con_.textContent=vid_value.value   
    var vid_ids = document.getElementById("vid_ids")  
    list_ids = JSON.parse(vid_ids)     
    var id_list = document.getElementById("id_list")
});
   
function open_resbar() {
    var resbar = document.getElementById("resbar")
    resbar.classList.toggle("show")
}
function open_resbar2() {
    var resbar = document.getElementById("resbar2")
    resbar.classList.toggle("show")
}
function open_resbar3() {
    var resbar = document.getElementById("resbar3")
    resbar.classList.toggle("show")
}
var vid_info_bg = document.getElementById("vid_info_bg")
function res_144p(res_id) {
    var res_144 = document.querySelector(`div[vid-info-id="${res_id}"]`)
    res_144.style.display="block";
    res_144.style.display="flex";
    var res_con = document.getElementById("vid_value")
    res_con.textContent="144p"
    
    var vid_ids = document.getElementById("vid_ids").value
    list_ids = JSON.parse(vid_ids)
    
    for (len_l in list_ids) {
        if (list_ids[len_l]!=res_id) {
            var rem = document.querySelector(`div[vid-info-id="${list_ids[len_l]}"]`)  
            rem.style.display="none"  
        }        
    }   
    var resbar = document.getElementById("resbar")
    resbar.classList.toggle("show")    
}
function res_360p(res_id) {
    var res_360 = document.querySelector(`div[vid-info-id="${res_id}"]`)
    res_360.style.display="block";
    res_360.style.display="flex";
    var res_con1 = document.getElementById("vid_value")
    res_con1.textContent="360p"
    
    var vid_ids = document.getElementById("vid_ids").value
    list_ids = JSON.parse(vid_ids)
    
    for (len_l in list_ids) {
        if (list_ids[len_l]!=res_id) {
            var rem = document.querySelector(`div[vid-info-id="${list_ids[len_l]}"]`)  
            rem.style.display="none"  
        }        
    }   
    var resbar = document.getElementById("resbar")
    resbar.classList.toggle("show")      
}

function res_720p(res_id) {
    var res_720 = document.querySelector(`div[vid-info-id="${res_id}"]`)
    res_720.style.display="block";
    res_720.style.display="flex";
    var res_con1 = document.getElementById("vid_value")
    res_con1.textContent="720"
    
    var vid_ids = document.getElementById("vid_ids").value
    list_ids = JSON.parse(vid_ids)
    
    for (len_l in list_ids) {
        if (list_ids[len_l]!=res_id) {
            var rem = document.querySelector(`div[vid-info-id="${list_ids[len_l]}"]`)  
            rem.style.display="none"  
        }        
    }   
    var resbar = document.getElementById("resbar")
    resbar.classList.toggle("show")        
}

function no_aud_func(no_aud_id,list_id) {
    var no_aud_tab = document.querySelector(`div[no-aud-id="${no_aud_id}"]`)
    no_aud_tab.style.display="block"     
    no_aud_tab.style.display="flex"
    
    var resbar2 = document.getElementById("resbar2")
    resbar2.classList.toggle("show")
    for (no_aud in list_id) {
        if (no_aud_id != list_id[no_aud]) {
            var hide_tabs = document.querySelector(`div[no-aud-id="${list_id[no_aud]}"]`)
            hide_tabs.style.display="none"
        }        
    }
}

function aud_func(aud_id,aud_list_id) {
    var aud_tab = document.querySelector(`div[aud-id="${aud_id}"]`)
    aud_tab.style.display="block"     
    aud_tab.style.display="flex"
    
    var resbar2 = document.getElementById("resbar3")
    resbar2.classList.toggle("show")
    for (new_aud in aud_list_id) {   
        if (aud_id != aud_list_id[new_aud]) {
            var hide_tabs = document.querySelector(`div[aud-id="${aud_list_id[new_aud]}"]`)
            hide_tabs.style.display="none"            
        }        
    }
}