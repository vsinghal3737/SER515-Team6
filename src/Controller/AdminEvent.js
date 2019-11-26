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
            $.post("/DeleteHistoryQuestions", user, function(data, status){
            console.log("Status: " + status);
            });
  			userList['Users'][item]['Grade'] = document.getElementById("user_table").rows[ctr].cells[4].firstChild.value;
            alert('User grade updated!');
		}
		ctr++;
	}	
}

function clearPage()
{
    var table = document.getElementById("user_table");
    while(document.getElementById("user_table").rows.length > 1)
    {
        table.deleteRow(1);
    }
}


function deleteUser(ev)
{   
    var username = ev.target.id;
    //document.getElementById(row_id).parentNode.removeChild(document.getElementById(row_id));
    //Add POST method to delete user in back-end
    user = {'Username': username}
    $.post("/DeleteUser", user, function(data, status){
            console.log("Status: " + status);
    });
    /*$.post("/DeleteHistoryQuestions", user, function(data, status){
            console.log("Status: " + status);
    }); */
    loadPage();
}

function loadPage()
{
	var ctr = 1;
    var tr = '';
    var row, col;
    var row, dropDown, option1, option2, option3, header, deleteUser;
    var table = document.getElementById("user_table");
    clearPage();
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
        col = row.insertCell(1);
        col.innerHTML = data['Users'][item]['FName'];
        col = row.insertCell(2);
        col.innerHTML = data['Users'][item]['LName'];
        col = row.insertCell(3);
        col.innerHTML = data['Users'][item]['Role'];
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
        col = row.insertCell(5);
        deleteUser = document.createElement('button');
        deleteUser.className = 'btn btn-danger';
        deleteUser.innerHTML = 'Delete';
        deleteUser.id = data['Users'][item]['Username'];
        deleteUser.setAttribute("onclick", "deleteUser(event)");
        col.appendChild(deleteUser);
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