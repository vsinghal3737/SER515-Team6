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
    else if(value == '+')
    {
        var operator = document.createElement('i');
        operator.className = 'fas fa-plus draggable-icon p-2';
        operator.style.fontSize = "45px";
        slot.appendChild(operator);
    }
    else if(value == '-')
    {
        var operator = document.createElement('i');
        operator.className = 'fas fa-minus draggable-icon p-2';
        operator.style.fontSize = "45px";
        slot.appendChild(operator);
    }
    else if(value == '=')
    {
        var operator = document.createElement('i');
        operator.className = 'fas fa-equals draggable-icon p-2';
        operator.style.fontSize = "45px";
        slot.appendChild(operator);
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

 function addQuestion(ev){
        var question = ev.target.value;
        var i;
        for(i = 0; i<question.length; i++)
        {
            addSlot(question.charAt(i));
        }
 }


function loadPage(){
    //Calling flask api to fetch questions
    $.get("/GetQuestions", function(data){
    //var question = JSON.parse(data);
    var item;
    for(item in data) {
        var questionDiv = document.createElement('div');
        questionDiv.className = 'row p-2';
        var questionButton = document.createElement('button');
        questionButton.className = 'btn btn-primary btn-lg btn-block';
        questionButton.setAttribute("onclick", "addQuestion(event)");
        questionButton.type = 'button';
        questionButton.value = data[item];
        questionButton.innerHTML = data[item];
        questionDiv.appendChild(questionButton);
        document.getElementById('question-list').appendChild(questionDiv);    
    }    
  });
}