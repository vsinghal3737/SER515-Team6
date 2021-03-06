var currentQuestion;
var answerctr = 0;
function clearCanvas(){
    var canvas = document.getElementById("canvas");
    while(canvas.childNodes.length>0) {
        canvas.removeChild(canvas.childNodes[0]);
    }
}

function clearAnswer() {
    var canvas = document.getElementById("canvas");
    for(item = 0; item < canvas.childNodes.length; item++)
        if(canvas.childNodes[item].id.search('answer') != -1) {
            while(canvas.childNodes[item].childNodes.length>0) {
                canvas.childNodes[item].removeChild(canvas.childNodes[item].firstChild);
            }
        }
}

function loadQuestionOnCanvas(question) {
    var i = 0;
    while(i < question.length)
        {
            var value = question.charAt(i);
            var slot = document.createElement('div');
            slot.className = 'col grid-item d-flex justify-content-center';
            document.getElementById("canvas").appendChild(slot);
            if(value >='0' && value<='9')
            {
                var nodeCopy = document.getElementById(question.charAt(i)).childNodes[1].cloneNode(true);
                //nodeCopy.style.fontSize = "45px";
                slot.appendChild(nodeCopy);
                
            }
            else if(value == '+')
            {
                var operator = document.createElement('p');
                operator.className = 'draggable-icon p-2';
                operator.innerHTML = '+';
                //operator.style.fontSize = "45px";
                slot.appendChild(operator);
            }
            else if(value == '-')
            {
                var operator = document.createElement('p');
                operator.className = 'draggable-icon p-2';
                operator.innerHTML = '-';
                //operator.style.fontSize = "45px";
                slot.appendChild(operator);
            }
            else if(value == '=')
            {
                var operator = document.createElement('p');
                operator.className = 'draggable-icon p-2';
                operator.innerHTML = '=';
                //operator.style.fontSize = "45px";
                slot.appendChild(operator);
            }
            else if(value == '*')
            {
                var operator = document.createElement('p');
                operator.className = 'draggable-icon p-2';
                operator.innerHTML = '*';
                //operator.style.fontSize = "45px";
                slot.appendChild(operator);
            }
            else if(value == '/')
            {
                var operator = document.createElement('p');
                operator.className = 'draggable-icon p-2';
                operator.innerHTML = '/';
                //operator.style.fontSize = "45px";
                slot.appendChild(operator);
            }
            else if(value == '<')
            {
                var operator = document.createElement('p');
                operator.className = 'draggable-icon p-2';
                operator.innerHTML = '<';
                //operator.style.fontSize = "45px";
                slot.appendChild(operator);
            }
            else if(value == '>')
            {
                var operator = document.createElement('p');
                operator.className = 'draggable-icon p-2';
                operator.innerHTML = '>';
                //operator.style.fontSize = "45px";
                slot.appendChild(operator);
            }
            else if(value == '(')
            {
                var operator = document.createElement('p');
                operator.className = 'draggable-icon p-2';
                operator.innerHTML = '(';
                //operator.style.fontSize = "45px";
                slot.appendChild(operator);
            }
            else if(value == ')')
            {
                var operator = document.createElement('p');
                operator.className = 'draggable-icon p-2';
                operator.innerHTML = ')';
                //operator.style.fontSize = "45px";
                slot.appendChild(operator);
            }

            else        //Only allow drop on empty slot
            {
                slot.id = 'answer'+answerctr;
				slot.className = slot.className + ' answerslot';
                answerctr++;
                slot.setAttribute("ondrop", "drop(event, this)"); 
                slot.setAttribute("ondragover", "allowDrop(event)");
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

 function loadQuestion(ev){
        clearCanvas();
        currentQuestion = ev.target.id;
        var question = ev.target.value;
        var i;
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
    var row, col, question;
    var item, index;
    removeCurrentQuestion();
    removeHistoryQuestions();
    $.get("/GetQuestionsPerStud", function(data){
    
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
        var keys = Object.keys(hist_data).reverse();
            for(item = 0; item < keys.length; item++) {
            tr = 'tr'+ctr;
            row = document.getElementById(tr);
            col = row.insertCell(0);
            col.innerHTML = ctr.toString();
            col.style = "text-align: center";
            col = row.insertCell(1);
            question = hist_data[keys[item]]['attempted_ans'];
            index = question.split('=');
            col.innerHTML = index[0];
            col.style = "text-align: center";
            col = row.insertCell(2);
            col.innerHTML = hist_data[keys[item]]['attempted_ans'];
            col.style = "text-align: center";
            col = row.insertCell(3);
            col.innerHTML = hist_data[keys[item]]['result'];
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
    equation = equation.split('=');
    lhs = equation[0];
    rhs = equation[1];
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

