import React, {useState} from 'react';
import {StyleSheet,View,Text,SafeAreaView,Image,TouchableHighlight } from 'react-native';

export default function App(){

  const moedas=[
    require('./imagens/1.png'),//Coroa
    require('./imagens/5.png'), // Cara
    // Giro da moeda
    require('./imagens/1.png'), require('./imagens/2.png'),
    require('./imagens/3.png'), require('./imagens/4.png'),
    require('./imagens/5.png'), require('./imagens/6.png'),
    require('./imagens/7.png'), require('./imagens/8.png')
  ]
  let moeda=0
  const maxGiros=5
  
  const [moedaAtual,setMoedaAtual]=useState(moedas[moeda])

  async function espera(tmp){
    function tempo(ms){
      return new Promise(resolve=>setTimeout(resolve,ms))
    }
    await tempo(tmp)
  }

  async function girarMoeda(){
    moeda=2
    for(let i=0;i<(maxGiros * 8);i++){
        moeda++
        if(moeda > 9){
          moeda=2
        }
        setMoedaAtual(moedas[moeda])
        await espera(50)
    }
 
  let res=Math.floor(Math.random()*10)+1
  if(res <= 5)
    res=0
  else
    res=1
  
    setMoedaAtual(moedas[res])
}
 

  return(
  <SafeAreaView style={estilos.container}>
    <View style={{alignItems:'center'}}>
      <Text style={estilos.titulo}>Cara ou Coroa</Text>
      <Image 
         source={moedaAtual}
         style={estilos.moeda}
      />     
      <TouchableHighlight 
          style={estilos.botao}
          onPress={()=>{girarMoeda()}}>
         <Text style={{color:'#fff', letterSpacing:2}}>GIRAR</Text>
      </TouchableHighlight>
     </View>
     
  </SafeAreaView>
  
  )
}


const estilos = StyleSheet.create({
 moeda:{
   padding:20,
   margin:20,
   resizeMode:'stretch',
   width:200,
   height:200
 },
 container:{
   flex:1,
   justifyContent:'center'
 },
 titulo:{
   fontSize:20,
   color:'#008',
   fontWeight:'bold',
   backgroundColor:'#0081',
   padding:10,
   borderRadius:10
 },
 botao:{
   borderWidth:2,
   padding:5,
   borderRadius:5,
   backgroundColor:'#00a',
   width:140,
   height:40,
   alignItems:'center',
   justifyContent:'center'
 }
});


