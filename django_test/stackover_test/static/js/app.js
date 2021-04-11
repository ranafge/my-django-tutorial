$.ajax({
    url ="{%url 'room_list'%}",
    type = 'get',
    dataType = 'json',
    success: function(data){
        let rows = '';
        data.rooms.forEatch(room=>{
            rows += `
		<tr>
			<td>${room.room_number}</td>
			<td>${room.name}</td>
			<td>${room.nobeds}</td>
			<td>${room.room_type}</td>
			<td>
				<button class="btn deleteBtn" data-id="${room.id}">Delete</button>
				<button class="btn updateBtn" data-id="${room.id}">Update</button>
			</td>
		</tr>`;
        });
        $('[#myTable](https://paper.dropbox.com/?q=%23myTable) > tbody').append(rows);
	$('.deleteBtn').each((i, elm) => {
		$(elm).on("click",  (e) => {
			deleteRoom($(elm))
		})
	})
    }

})