import logo from "./logo.svg";
import "@aws-amplify/ui-react/styles.css";
import {
  withAuthenticator,
  Button,
  Heading,
  Image,
  View,
  Card,
} from "@aws-amplify/ui-react";

import { API } from 'aws-amplify';

async function startGame() {
    const apiName = 'apibcb6604c';
    const path = '/game/start';
    const options = {
        headers: {}
    };

    const response = await API.post(apiName, path, options);
    console.log(response);
}


function App({ signOut }) {
  return (
    <View className="App">
      <Card>
        <Image src={logo} className="App-logo" alt="logo" />
        <Heading level={1}>We now have Auth!</Heading>
        <Button onClick={startGame}>Start Game</Button>
      </Card>
      <Button onClick={signOut}>Sign Out</Button>
    </View>
  );
}

export default withAuthenticator(App);