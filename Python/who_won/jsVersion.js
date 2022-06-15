
function getCols(board){
	var cols = [];
	for (var i = 0; i<board.length; i++){
		col = []; 
		for (var j = 0; j<board.length; j++){
  			col.push(board[j][i]);
  		}
  		cols.push(col)  		
  	}
  	return cols
}


function count(arr,ele){
	var total = 0;
	for (const element of arr){
		if (element === ele){
			total++;
		}
	}
	return total;
}


function whoWon(board) {
  	
  	var l = board.length;
  	var scoreX = 0;
  	var scoreO = 0;
  	var lr = [[board[0][0],board[1][1],board[2][2]]];
  	var rl = [[board[0][l-1],board[1][l-2],board[2][l-3]]];
  	var cols = getCols(board);
  	var rows = board;

  	for (const arr of [lr, rl, cols, rows]){
  		for (const lst of arr){
			if(count(lst,"X") === 3){
  				scoreX += 1;
  			}
  			else if(count(lst,"O") === 3){
  				scoreO += 1;
  			}  			
  		}
  	}
  	
  	return scoreX > scoreO ? "X" : scoreO > scoreX ? "O" : "Tie"
}

whoWon([
	["X", "O", "X"],
    ["X", "O", "O"],
    ["X", "X", "O"]])