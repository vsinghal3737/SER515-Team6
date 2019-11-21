var userList;

function saveChanges()
{
	//alert(document.getElementById("user_table").rows[1].cells[4].firstChild.value);
	var ctr = 1;
	for(item in userList['Users']) {
		if(document.getElementById("user_table").rows[ctr].cells[4].firstChild.value != userList['Users'][item]['Grade']) {
			user = {'Username': document.getElementById("user_table").rows[ctr].cells[0].innerHTML,
				'Grade': document.getElementById("user_table").rows[ctr].cells[4].firstChild.value
			};
			$.post("/UpdateGrade", user, function(data, status){
    			console.log("Status: " + status);
  			});
  			userList['Users'][item]['Grade'] = document.getElementById("user_table").rows[ctr].cells[4].firstChild.value;
            alert('User grade updated!');
		}
		ctr++;
	}
	
	
}

function loadPage()
{
	var ctr = 1;
    var tr = '';
    var row, col;
    var row, dropDown, option1, option2, option3, header;
    var table = document.getElementById("user_table");
 	$.get("/GetAllUsers", function(data){
    var item;
    userList = data;
    //Parsing JSON object to create the user list
    for(item in data['Users']) {
        tr = 'tr'+ctr;
        row = table.insertRow(ctr);
        row.id = tr;
        col = row.insertCell(0);
        col.innerHTML = data['Users'][item]['Username'];
        //col.style = "text-align: center";
        col = row.insertCell(1);
        col.innerHTML = data['Users'][item]['FName'];
        //col.style = "text-align: center";
        col = row.insertCell(2);
        col.innerHTML = data['Users'][item]['LName'];
        //col.style = "text-align: center";
        col = row.insertCell(3);
        col.innerHTML = data['Users'][item]['Role'];
        //col.style = "text-align: center";
        col = row.insertCell(4);
        dropDown = document.createElement('SELECT');
        option = document.createElement('option');
        if (data['Users'][item]['Grade'] == 1){
        	option.text = '1';
        	dropDown.add(option);
	        option = document.createElement('option');
	        option.text = '4';
	        dropDown.add(option);
        }
        else {        	
        	option.text = '4';
        	dropDown.add(option);
	        option = document.createElement('option');
	        option.text = '1';
	        dropDown.add(option);
        }
        
        col.appendChild(dropDown);
        ctr++;
    }    
    });
		
            
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