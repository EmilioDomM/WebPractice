import React, { useState } from "react";
import Button from "@/components/Button";

function contador() {
  const [contador, setContador] = useState(0);

  function incrementa() {
    setContador(contador + 1);
    console.log(contador);
  }

  function decrementa() {
    setContador(contador - 1);
    console.log(contador);
  }

  function reset() {
    setContador(0);
    console.log(contador);
  }

  return (
    <div>
      <p>Contador: {contador}</p>
      <Button color="red" onClick={incrementa}>
        Incementar
      </Button>
      <Button color="blue" onClick={decrementa}>
        decrementa
      </Button>
      <Button color="green" onClick={reset}>
        Reset
      </Button>
    </div>
  );
}

export default contador;
