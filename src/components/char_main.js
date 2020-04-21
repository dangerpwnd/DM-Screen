import React from "react"
import CharClass from "./char_class"
import CharSpeed from "./char_speed"
import CharAc from "./char_ac"

const CharMain = () => {
    return(
            <div className="playerMainGrid">
                    <h1 className="border">Bartos Donadarion</h1>
                    <CharClass />
                    <CharSpeed />
                    <CharAc />
            </div>
    )
}

export default CharMain