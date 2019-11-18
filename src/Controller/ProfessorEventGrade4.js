function addSlot() {
	var slot = document.createElement('div');
	slot.className = 'canvas-item d-flex justify-content-center';
	slot.setAttribute("ondrop", "drop(event, this)"); 
	slot.setAttribute("ondragover", "allowDrop(event)");
	document.getElementById('canvas').appendChild(slot);
}

function clearCanvas(){
    var canvas = document.getElementById("canvas");
    while(canvas.childNodes.length>0) {
        canvas.removeChild(canvas.childNodes[0]);
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
        var childNode = document.getElementById(id).childNodes[1];
        var nodeCopy = childNode.cloneNode(true);
        nodeCopy.style.fontSize = "45px";
        el.appendChild(nodeCopy);
        ev.stopPropagation();
        return false;
}