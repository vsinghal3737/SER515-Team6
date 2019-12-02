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

function clearAnswer() {
    var canvas = document.getElementById("canvas");
    for(item = 0; item < canvas.childNodes.length; item++)
        if(canvas.childNodes[item].id.search('answer') != -1) {
            while(canvas.childNodes[item].childNodes.length>0) {
                canvas.childNodes[item].removeChild(canvas.childNodes[item].firstChild);
            }
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
    if(eval(equation)!= Nan){
       alert('The answer is' eval(equation));
    }
    else{
        alert('Invalid expression');
    }

}
