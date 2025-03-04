import React, { useState, useEffect } from 'react';  
import { View, Text, Button, StyleSheet } from 'react-native';  

const TrafficApp = () => {  
  const [route, setRoute] = useState(null);  
  const [alerts, setAlerts] = useState([]);  

  useEffect(() => {  
    fetch('http://localhost:5000/route')  
      .then(res => res.json())  
      .then(data => setRoute(data));  

    fetch('http://localhost:5000/alerts')  
      .then(res => res.json())  
      .then(data => setAlerts(data));  
  }, []);  

  return (  
    <View style={styles.container}>  
      <Text style={styles.header}>Optimal Route:</Text>  
      <Text>{route?.summary || "Calculating..."}</Text>  
      <Text style={styles.header}>Alerts:</Text>  
      {alerts.map((alert, idx) => (  
        <Text key={idx}>{alert.message}</Text>  
      ))}  
      <Button title="Refresh" onPress={() => {/* Logic */}} />  
    </View>  
  );  
};  

const styles = StyleSheet.create({  
  container: { padding: 20 },  
  header: { fontWeight: 'bold', marginTop: 10 }  
});  

export default TrafficApp;  