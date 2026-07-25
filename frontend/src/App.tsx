import { PhoneFrame } from "./components/PhoneFrame";

import { Chat } from "./components/Chat";
import "@mantine/core/styles.css";

function App() {
  return (
    <PhoneFrame>
      <Chat />
    </PhoneFrame>
  );
}

export default App;
