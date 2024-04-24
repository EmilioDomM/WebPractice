import React from "react";
import Saludo from "@/components/Saludo";
import Card from "@/components/Card";
import Button from "@/components/Button";

function index() {
  return (
    <div>
      <Saludo nombre="Emilio" apellido="Dominguez" />
      <Card>
        <hi>Titulo</hi>
        <p>Ejemplo de card</p>
      </Card>

      <Button color="red" onClick={incrementar}>Incrementar</Button>
      
    </div>
  );
}

export default index;
