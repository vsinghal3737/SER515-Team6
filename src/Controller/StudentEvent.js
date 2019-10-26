var currentQuestion;
var qctr = 0;
var questionList;
function clearCanvas(){
    var canvas = document.getElementById("canvas");
    while(canvas.childNodes.length>0) {
        canvas.removeChild(canvas.childNodes[0]);
    }
}

function loadQuestionOnCanvas(value) {
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

 function loadQuestion(ev){
        clearCanvas();
        currentQuestion = ev.target.id;
        var question = ev.target.value;
        var i;
        for(i = 0; i<question.length; i++)
        {
            loadQuestionOnCanvas(question.charAt(i));
        }
 }



function loadPage(){
    //Calling flask api to fetch questions
    $.get("/GetQuestions", function(data){
    var item;
    questionList = data;
    //Parsing JSON object to create the questions
    for(item in data['questions']) {
        var questionDiv = document.createElement('div');
        questionDiv.className = 'row p-2';
        var questionButton = document.createElement('button');
        questionButton.className = 'btn btn-primary btn-lg btn-block';
        questionButton.setAttribute("onclick", "loadQuestion(event)");
        questionButton.type = 'button';
        questionButton.id = data[item]['QuestionID'];
        qctr++;
        questionButton.value = data[item]['Question'];
        questionButton.innerHTML = data[item]['Question'];
        questionDiv.appendChild(questionButton);
        document.getElementById('question-list').appendChild(questionDiv);    
    }    
    });

    /*$.get("/GetHistoryQuestions", function(data){
        for(item in data['Questions']) {

        }
    }
    */
}

function removeCurrentQuestion() {
    var questionFrame = document.getElementById("question-list");
    questionFrame.removeChild(document.getElementById(currentQuestion).parentNode);
}

function submitAnswer(ev){
    var equation = '';
    var lhs, rhs;
    var answer = {
        'QuestionID': '',
        'Result': '',
        'Date': '',
        'Answer': ''
    }
    var canvas = document.getElementById("canvas");
    while (canvas.childNodes.length>=1) {  
        if(canvas.childNodes[0].firstChild.className.search('fa-plus') != -1)
        {
            equation = equation+'+';
        }
        else if(canvas.childNodes[0].firstChild.className.search('fa-minus') != -1)
        {
            equation = equation+'-';
        }
        else if(canvas.childNodes[0].firstChild.className.search('fa-equals') != -1)
        {
            lhs = equation;
            equation = '';
        }
        else
        {
            equation = equation+canvas.childNodes[0].firstChild.innerHTML;
        }
        canvas.removeChild(canvas.childNodes[0]);
    }
    rhs = equation;
    if(eval(lhs) == eval(rhs))
        answer['Result'] = 'Pass';
    else
        answer['Result'] = 'Fail';
    answer['QuestionID'] = currentQuestion;
    var tzoffset = (new Date()).getTimezoneOffset() * 60000; //offset in milliseconds
    var localISOTime = (new Date(Date.now() - tzoffset)).toISOString().slice(0, 19).replace('T', ' ');
    answer['Date'] = localISOTime;
    alert(answer['Result']);
    if(answer['Result'] == 'Pass')
        removeCurrentQuestion();    
    //Should contain code to send POST request to back-end with the submitted answer
    //Access JSON object of current question using: questionList[currentQuestion]

}