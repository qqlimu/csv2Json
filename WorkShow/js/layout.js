function show(index){
    var elem=document.getElementById('caidan'+index);
    if(elem.style.display=='none')
        elem.style.display='block';
    else
        elem.style.display='none';
}