import React from "react"
import CharClass from "./char_class"
import CharSpeed from "./char_speed"
import CharAc from "./char_ac"

function CharMain() {
    return(
        <div>
            <h1>Bartos Donadarion</h1>
            <CharClass />
            <CharSpeed />
            <CharAc />
        </div>
    )
}

export default CharMain