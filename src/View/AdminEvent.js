function saveChanges()
{
	
	var selectOption1=document.getElementById("select_tag1").value;
	var selectOption2=document.getElementById("select_tag2").value;
	var selectOption3=document.getElementById("select_tag3").value;
	
	
}

function loadPage()
{
	var ctr = 1;
    var tr = '';
    var row, col;
    var row, dropDown, option1, option2, option3;
    var table = document.getElementById("user_table");
    tr = 'tr'+ctr;
            row = document.createElement('tr');
            row.id = tr;
            col = row.insertCell(0);
            col.innerHTML = 'ankitvutu';//user_data[item]['Username'];
            col.style = "text-align: center";
            col = row.insertCell(1);
            col.innerHTML = 'Ankit';//user_data[item]['FName'];
            col.style = "text-align: center";
            col = row.insertCell(2);
            col.innerHTML = 'Vutukuri';//user_data[item]['LName'];
            col.style = "text-align: center";
            col = row.insertCell(3);
            col.innerHTML = 'Student';//hist_data[item]['Role'];
            col.style = "text-align: center";
            col = row.insertCell(4);
            dropDown = document.createElement('SELECT');
            option1 = document.createElement('option');
            option1.text = '1';
            option2 = document.createElement('option');
            option2.text = '2';
            option3 = document.createElement('option');
            option4.text = '3';
            ctr++;
            table.insertRow(row);
	/*$.get("/GetHistoryQuestions", function(hist_data){
        hist_data = hist_data['Questions'];
        for(item = Object.keys(hist_data).length; item>=0; item--) {
            
        }
    });*/
}

function search()
{	
	var searchValue=document.getElementById("search_text").value;
	console.log(searchValue);
	//document.getElementById("1").innerHTML=searchValue;
}