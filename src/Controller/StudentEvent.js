function addSlot() {
	var slot = document.createElement('div');
	slot.className = 'canvas-item d-flex justify-content-center';
	slot.setAttribute("ondrop", "drop(event)"); 
	slot.setAttribute("ondragover", "allowDrop(event)");
	document.getElementById('canvas').appendChild(slot);
}
function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}
function drop(ev) {
        ev.preventDefault();
        var id = ev.dataTransfer.getData("text");
        //var isLeft = "example1" == id || "example2" == id;
        var childNode = document.getElementById(id).childNodes[1];
        var nodeCopy = childNode.cloneNode(true);
        //nodeCopy.id = id + ev.target.id;
        // clean target space if needed 
        nodeCopy.style.fontSize = "45px";
        ev.target.appendChild(nodeCopy);
        ev.stopPropagation();
        return false;
}

