import React,{useState} from 'react';
import {SafeAreaView,StyleSheet,View,Text,TextInput,TouchableHighlight} from 'react-native';

export default function App(){

  const [valor1,setValor1]=useState(0)
  const [valor2,setValor2]=useState(0)
  const [resultado,setResultado]=useState(0)

  const soma = ()=>{
    setResultado(Number(valor1) + Number(valor2))
  }

  return(
    <SafeAreaView style={estilos.container}>
    <Text>Calculadora</Text>
    <TextInput
      style={estilos.display}
      value={String(valor1)}
      onChangeText={(texto)=>{setValor1(parseInt(texto))}}
      keyboardType='numeric'
    ></TextInput>
     <TextInput
      style={estilos.display}
      value={String(valor2)}
      onChangeText={(texto)=>{setValor2(texto)}}
      keyboardType='numeric'
    ></TextInput>
     <TextInput
      style={estilos.display}
      value={String(resultado)}
      onChangeText={(texto)=>{setResultado(parseInt(texto))}}
      keyboardType='numeric'
    ></TextInput>
    <TouchableHighlight 
    onPress={()=>soma()}
    style={{backgroundColor:'#bbb',color:'#fff', padding:10, alignItems:'center'}}><Text>SOMAR</Text></TouchableHighlight>
      
    </SafeAreaView>
  )
}


const estilos = StyleSheet.create({
  container:{
    padding:10
  },
  display:{
    marginTop:10,
    borderWidth:1,
    borderRadius:10,
    padding:10

  }
});


