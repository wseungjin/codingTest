const readline = require('readline');

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
}).on('line', (line) => {
	const length = Number(line);
    	
	async function max10(basic,index){
		for(let i = 0 ; i < index ; i++){
            await readCharacter(basic+i, (error, result) => {
                process.stdout.write(result)
            });
		}
		rl.close();
	}


	async function ioProcessing(){
		let start = 0
		let cur = 0
		while(cur < length){
            if(cur + 10 > length){
                break
            }
            await max10(cur,10)
            cur = cur + 10
		}
		for(let i = cur ; i < length ; i++){
			 await max10(cur,1)
		}
		rl.close();
	}

	ioProcessing();

});

