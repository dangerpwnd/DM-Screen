import React from "react"
import Char_Weapon from "./char_weapon"

function CharAttack() {
    return(
        <div className="playerAttackGrid playerFlexCol">
            <div className="border">
                <Char_Weapon />
                <Char_Weapon />
                <Char_Weapon />
            </div>
        </div>
    )
}

export default CharAttack