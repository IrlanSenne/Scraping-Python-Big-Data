// const axios = require('axios')
// const cheerio = require('cheerio')
// const fs = require('fs')

// const fetchData = async (url)=>{
//     const result = await axios.get(url)
//     return result.data
// }

// const main = async ()=>{
//  for(let i=1;i<=50;i++){
//     fs.appendFile(`genesis.json`, `"c${i}":{`+`\n`,
//     function (err) {
//      if (err) throw err; 
  
  
//   });
//     const content = await fetchData('https://www.bibliaonline.com.br/acf/gn/'+i)
//     const $ = cheerio.load(content, { decodeEntities: false })    
    
// //https://www.abibliadigital.com.br/api/verses/:version/:abbrev/:chapter

//     $('article').find('div > div > p').each((ind, e)=>{
//        //const indice = i+1
//        var versiculo = $(e).text()                      
//        var numVer = versiculo.substr(0, 2)
//        //FORMATAR PARA JSON

//        fs.appendFile(`genesis.json`, `"${numVer.trim()}":`+ '"'+versiculo.replace(numVer,"")+'",'+`\n`,
//        function (err) {
//         if (err) throw err; 
     
//         console.log(numVer);
//      });
//       //console.log(num + '.' +versiculo.replace('Copyright© 2017 por Editora Mundo Cristão. Todos os direitos reservados em língua portuguesa. A Nova Versão Transformadora (NVT) e seu logotipo são marcas registradas. Usados com permissão.',' ').replace(num,''))
//     })
//     fs.appendFile(`genesis.json`, `},${'\n'}`,
//     function (err) {
//      if (err) throw err; 
  

//   });
   
//  }
       
    
   
    
    
// }

// main()

import teste from './teste.json'

console.log(teste.c1[0])