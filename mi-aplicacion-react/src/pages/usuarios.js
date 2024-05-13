import React, { useState, useEffect } from "react";
import axios from "axios";

function usuarios() {
  const [usuarios, setUsuarios] = useState([]);

  useEffect(() => {
    axios
    .get("https://jsonplaceholder.typicode.com/users")
    .then(response => {
      setUsuarios(response.data);
      console.log(response.data);
    });
  }, []);

  return (
    <div className="flex dlex-vol items-center justifiy-center">
      <h1 className="text-2xl font-bold">Lista de Usuarios</h1>
      <ul>
        {usuarios.map((usuario) => (
          <li key={usuario.id}>
            {usuario.name} - {usuario.email}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default usuarios;
