var nodeCounter = 1;


//No longer needed
function addSlot() {
	var slot = document.createElement('div');
	slot.className = 'canvas-item d-flex justify-content-center';
    slot.setAttribute("draggable", "true");
    slot.setAttribute("ondragstart", "drag(event)");
    slot.id = 'canvas'+nodeCounter;
    nodeCounter++;
	document.getElementById('canvas').appendChild(slot);
}

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
        nodeCopy.id = 'canvasitem'+nodeCounter;
        nodeCopy.setAttribute("ondragover", "allowDrop(event)");
        nodeCopy.setAttribute("ondrop", "dropOnNode(event, this)");
        nodeCopy.setAttribute("ondragleave", "onDragLeave(event)");
        nodeCounter++;
        if(document.getElementById('canvas').childNodes.length < 9)
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
        nodeCopy.id = 'canvasitem'+nodeCounter;
        nodeCopy.setAttribute("ondragover", "allowDrop(event)");
        nodeCopy.setAttribute("ondrop", "dropOnNode(event, this)");
        nodeCopy.setAttribute("ondragleave", "onDragLeave(event)");
        nodeCounter++;
        if(document.getElementById('canvas').childNodes.length < 9)
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
function removeHistoryQuestions()
{
    var tr = '';
    var ctr = 1;
    var row;
    for(ctr = 1; ctr<=5; ctr++)
    {
        tr = 'tr'+ctr;
        row = document.getElementById(tr);
        while(row.firstChild)
            row.removeChild(row.firstChild);
    }  
}

function loadPage() {
    var ctr = 1;
    var tr = '';
    var row, col;
    removeHistoryQuestions();
    $.get("/GetQuestionsPerGrade", function(hist_data){
        hist_data = hist_data['Questions'];
        var keys = Object.keys(hist_data).reverse();
        for(item = 0; item < keys.length; item++) {
            tr = 'tr'+ctr;
            row = document.getElementById(tr);
            col = row.insertCell(0);
            col.innerHTML = ctr.toString();
            col.style = "text-align: center";
            col = row.insertCell(1);
            col.innerHTML = hist_data[keys[item]]['question'];
            col.style = "text-align: center";
            col = row.insertCell(2);
            col.innerHTML = hist_data[keys[item]]['submitted_on'].slice(0, 17);
            col.style = "text-align: center";
            ctr++;
        }
    });
}

function submitQuestion(ev){
    var question = '';
    var result;
    var canvas = document.getElementById("canvas");
    while (canvas.childNodes.length>=1) {  
        if(canvas.childNodes[0].firstChild.className.search('fa-plus') != -1)
        {
            question = question+'+';
        }
        else if(canvas.childNodes[0].firstChild.className.search('fa-minus') != -1)
        {
            question = question+'-';
        }
        else
            question = question+canvas.childNodes[0].firstChild.innerHTML;
        canvas.removeChild(canvas.childNodes[0]);
    }
    try {
    eval(question); 
    } 
    catch (e) {
        alert("INVALID QUESTION FORMAT!");
        return;
    }
    if(eval(question) == null){
        alert("EMPTY QUESTION!");
        return;
    }
    question = question+'=_';
    var tzoffset = (new Date()).getTimezoneOffset() * 60000; //offset in milliseconds
    var localISOTime = (new Date(Date.now() - tzoffset)).toISOString().slice(0, 19).replace('T', ' ');
    question_json = {'Question': question,
        'Date': localISOTime,
    };
    $.post("/SubmitQuestion", question_json);
    alert('Question Created Successfully!');
    loadPage();

    
    //Should contain code to send POST request to back-end with the submitted answer
    //Access JSON object of current question using: questionList[currentQuestion]

}