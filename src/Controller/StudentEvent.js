var currentQuestion;
function clearCanvas(){
    var canvas = document.getElementById("canvas");
    while(canvas.childNodes.length>0) {
        canvas.removeChild(canvas.childNodes[0]);
    }
}


function loadQuestionOnCanvas(question) {
    var i = 0;
    while(i < question.length)
        {
            var value = question.charAt(i);
            var slot = document.createElement('div');
            slot.className = 'canvas-item d-flex justify-content-center';
            slot.setAttribute("ondrop", "drop(event, this)"); 
            slot.setAttribute("ondragover", "allowDrop(event)");
            document.getElementById("canvas").appendChild(slot);
            if(value >='0' && value<='9')
            {
                while(question.charAt(i) >= '0' && question.charAt(i) <= '9')
                {
                    var nodeCopy = document.getElementById(question.charAt(i)).childNodes[1].cloneNode(true);
                    nodeCopy.style.fontSize = "45px";
                    slot.appendChild(nodeCopy);
                    i++;
                }
                i--;
                
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
            i++;
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
        if(el.hasChildNodes()) {
            if(el.firstChild.tagName == 'I')
                return;
        }
        
        var id = ev.dataTransfer.getData("text");
        var childNode = document.getElementById(id).childNodes[1];
        var nodeCopy = childNode.cloneNode(true);
        //nodeCopy.id = id + ev.target.id;
        nodeCopy.style.fontSize = "45px";
        // Only allow drop if slot does not contain operator and restricting number of digits to two.
        if(el.childNodes.length <= 1)
            el.appendChild(nodeCopy);

        
        ev.stopPropagation();
        return false;
}

 function loadQuestion(ev){
        clearCanvas();
        currentQuestion = ev.target.id;
        var question = ev.target.value;
        var i;
        matches = question.match(/\d+/g);
        loadQuestionOnCanvas(question);
        
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

function loadPage(){
    //Calling flask api to fetch questions
    var ctr = 1;
    var tr = '';
    var row, col;

    removeCurrentQuestion();
    removeHistoryQuestions();
    loadQuestionOnCanvas("_+_=40");
    $.get("/GetQuestionsPerStud", function(data){
    var item;
    data = data['Questions']
    //Parsing JSON object to create the questions
    for(item in data) {
        var questionDiv = document.createElement('div');
        questionDiv.className = 'row p-2';
        var questionButton = document.createElement('button');
        questionButton.className = 'btn btn-primary btn-lg btn-block';
        questionButton.setAttribute("onclick", "loadQuestion(event)");
        questionButton.type = 'button';
        questionButton.id = 'Q'+data[item]['id'].toString();
        questionButton.value = data[item]['question'];
        questionButton.innerHTML = data[item]['question'];
        questionDiv.appendChild(questionButton);
        document.getElementById('question-list').appendChild(questionDiv);    
    }    
    });
    $.get("/GetHistoryQuestions", function(hist_data){
        hist_data = hist_data['Questions'];
        for(item = Object.keys(hist_data).length; item>=0; item--) {
            tr = 'tr'+ctr;
            row = document.getElementById(tr);
            col = row.insertCell(0);
            col.innerHTML = ctr.toString();
            col.style = "text-align: center";
            col = row.insertCell(1);
            col.innerHTML = hist_data[item]['attempted_ans'];
            col.style = "text-align: center";
            col = row.insertCell(2);
            col.innerHTML = hist_data[item]['attempted_ans'];
            col.style = "text-align: center";
            col = row.insertCell(3);
            col.innerHTML = hist_data[item]['result'];
            col.style = "text-align: center";
            ctr++;
        }
    });
    
}

function removeCurrentQuestion() {
    var questionFrame = document.getElementById("question-list");
    while (questionFrame.firstChild) {
    questionFrame.removeChild(questionFrame.firstChild);
  }
}



function submitAnswer(ev){
    var equation = '';
    var lhs, rhs, result;
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
            if(canvas.childNodes[0].childNodes.length > 1)
                equation = equation+canvas.childNodes[0].childNodes[1].innerHTML;
            
        }
        canvas.removeChild(canvas.childNodes[0]);
    }
    rhs = equation;
    if(eval(lhs)==eval(rhs))
        result = 'Pass'
    else
        result = 'Fail'
    equation = lhs+'='+rhs;
    var tzoffset = (new Date()).getTimezoneOffset() * 60000; //offset in milliseconds
    var localISOTime = (new Date(Date.now() - tzoffset)).toISOString().slice(0, 19).replace('T', ' ');
    answer = {'His_QuesID': currentQuestion,
        'Result': result,
        'Date': localISOTime,
        'Attempt': equation
    };
    $.post("/SubmitAnswer", answer);
    if(result == 'Pass')
        alert("Submitted answer is correct");
    else
        alert("Submitted answer is wrong");
    loadPage();
    //Should contain code to send POST request to back-end with the submitted answer
    //Access JSON object of current question using: questionList[currentQuestion]

}

