function addSlot(value) {
    var slot = document.createElement('div');
    slot.className = 'canvas-item d-flex justify-content-center';
    slot.setAttribute("ondrop", "drop(event, this)"); 
    slot.setAttribute("ondragover", "allowDrop(event)");
    document.getElementById("canvas").appendChild(slot);
    
    if(value >='0' && value<='9')
    {
        var nodeCopy = document.getElementById(value).childNodes[1].cloneNode(true);
        nodeCopy.style.fontSize = "45px";
        slot.appendChild(nodeCopy);
    }


}



function allowDrop(ev) {
     ev.preventDefault(); 
   
}


function drag(ev) {
          ev.dataTransfer.setData("text", ev.target.id);
   
}

function drop(ev, el) {
        ev.preventDefault();
        var id = ev.dataTransfer.getData("text");
        //var isLeft = "example1" == id || "example2" == id;
        var childNode = document.getElementById(id).childNodes[1];
        var nodeCopy = childNode.cloneNode(true);
        //nodeCopy.id = id + ev.target.id;
        // clean target space if needed 
        nodeCopy.style.fontSize = "45px";
        el.appendChild(nodeCopy);
        
        ev.stopPropagation();
        return false;
}