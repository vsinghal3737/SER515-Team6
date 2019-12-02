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
        //nodeCopy.id = id + ev.target.id;
        // Only allow drop if slot does not contain operator and restricting number of digits to two.
        if(el.childNodes.length <= 2)
            el.appendChild(nodeCopy);

        
        ev.stopPropagation();
        return false;
}