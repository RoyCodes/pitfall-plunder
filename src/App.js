import logo from "./logo.svg";
import React, { useState } from 'react';
import "@aws-amplify/ui-react/styles.css";
import {
  withAuthenticator,
  Button,
  Heading,
  Image,
  View,
  Card,
}
from "@aws-amplify/ui-react";

import { API } from 'aws-amplify';

function App({ signOut }) {
  const [gameOutput, setGameOutput] = useState("");
  const [userInput, setUserInput] = useState("");


  async function startGame() {
    const apiName = 'apibcb6604c';
    const path = '/game/start';
    const options = {
      headers: {}
    };

    const response = await API.post(apiName, path, options);
    console.log(response);
    setGameOutput(response.data.message); // update the game's output with response
  }

  async function sendInput() {
    const apiName = 'myAPIName'; // replace with your API name
    const path = '/game/{gameId}/input';
    const options = {
      headers: {}, // any additional headers
      body: { input: userInput } // pass the user's input here
    };

    const response = await API.post(apiName, path, options);
    console.log(response);
    setGameOutput(response.data.message); // update the game's output with the new response
  }

  return (
    <View className="App">
      <Card>
        <Image src={logo} className="App-logo" alt="logo" />
        <Heading level={1}>We now have Auth!</Heading>
        <p>{gameOutput}</p>
        <input value={userInput} onChange={e => setUserInput(e.target.value)} />
        <Button onClick={sendInput}>Send Input</Button>
        <Button onClick={startGame}>Start Game</Button>
        <Button onClick={signOut}>Sign Out</Button>
      </Card>
    </View>
  );
}

export default withAuthenticator(App);