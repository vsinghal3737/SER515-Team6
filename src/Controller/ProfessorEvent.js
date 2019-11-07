function allowDrop(ev) {
   
}


function drag(ev) {
   
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