var nodeCounter = 1;
function clearCanvas(){
    var canvas = document.getElementById("canvas");
    while(canvas.childNodes.length>0) {
        canvas.removeChild(canvas.childNodes[0]);
    }
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function allowDrop(ev) {
    ev.preventDefault();
    var className = ev.target.className;
    if(ev.target.id.search('canvasitem') != -1)
        ev.target.className = "col grid-item d-flex justify-content-center drag-over";
    else if(ev.target.parentNode.id.search('canvasitem') != -1)
        ev.target.parentNode.className = "col grid-item d-flex justify-content-center drag-over";
}

function onDragLeave(ev) {
    if(ev.target.id.search('canvasitem') != -1)
        ev.target.className = "col grid-item d-flex justify-content-center";
    else if(ev.target.parentNode.id.search('canvasitem') != -1)
        ev.target.parentNode.className = "col grid-item d-flex justify-content-center";
}
//Called when node is dragged into canvas
function dropOnCanvas(ev, el) {
        ev.preventDefault();
        var id = ev.dataTransfer.getData("text");
        var childNode = document.getElementById(id);
        var nodeCopy = childNode.cloneNode(true);
        if(nodeCopy.id == "answer")
            nodeCopy.firstChild.innerHTML = " ";
        nodeCopy.id = 'canvasitem'+nodeCounter;
        nodeCopy.setAttribute("ondragover", "allowDrop(event)");
        nodeCopy.setAttribute("ondrop", "dropOnNode(event, this)");
        nodeCopy.setAttribute("ondragleave", "onDragLeave(event)");
        nodeCounter++;
        if(document.getElementById('canvas').childNodes.length < 15)
            document.getElementById('canvas').appendChild(nodeCopy);
        else
            alert("Canvas is full");
        ev.stopPropagation();
        return false;
}

function dropOnNode(ev, el) {
    ev.preventDefault();
    var id = ev.dataTransfer.getData("text");
    var childNode = document.getElementById(id);
    var nodeCopy = childNode.cloneNode(true);
    if(childNode.id.search('canvasitem') != -1) {
        nodeCopy.id = childNode.id;
        document.getElementById('canvas').removeChild(childNode);
        document.getElementById('canvas').insertBefore(nodeCopy, el);
    }
    else {
        if(nodeCopy.id == "answer")
            nodeCopy.firstChild.innerHTML = " ";
        nodeCopy.id = 'canvasitem'+nodeCounter;
        nodeCopy.setAttribute("ondragover", "allowDrop(event)");
        nodeCopy.setAttribute("ondrop", "dropOnNode(event, this)");
        nodeCopy.setAttribute("ondragleave", "onDragLeave(event)");
        nodeCounter++;
        if(document.getElementById('canvas').childNodes.length < 15)
            document.getElementById('canvas').insertBefore(nodeCopy, el);
        else
            alert("Canvas is full");
    }
    el.className = "col grid-item d-flex justify-content-center";
    ev.stopPropagation();
    return false;
}
//Called when node is dragged away from canvas to delete
function dropToRemove(ev, el) {
    ev.preventDefault();
    var id = ev.dataTransfer.getData("text");
    var node = document.getElementById(id);
    document.getElementById('canvas').removeChild(node);
    ev.stopPropagation();
    return false;
}
function submitAnswer(ev){
    var equation = '';
    var lhs, rhs, result;
    var canvas = document.getElementById("canvas");
    while (canvas.childNodes.length>=1) {          
        if(canvas.childNodes[0].id.search('answer') != -1) {
            while(canvas.childNodes[0].childNodes.length>0) {
                equation = equation+canvas.childNodes[0].firstChild.innerHTML;
                canvas.childNodes[0].removeChild(canvas.childNodes[0].firstChild);
            }
        }
        else
            equation = equation+canvas.childNodes[0].firstChild.innerHTML;
        canvas.removeChild(canvas.childNodes[0]);
    }
    if(eval(equation)!= Nan){
       alert('The answer is' + eval(equation));
    }
    else{
        alert('Invalid expression');
    }

}
