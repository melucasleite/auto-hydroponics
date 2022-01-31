import Button from "@mui/material/Button";
import PersistentDrawerLeft from "./Menu.tsx";

function App() {
  return (
    <PersistentDrawerLeft>
      <Button variant="contained">Hello World</Button>
    </PersistentDrawerLeft>
  );
}

export default App;
