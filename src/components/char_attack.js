import React from "react";
import Char_Weapon from "./char_weapon";

const charAttack = () => {
    return(
        <div className="playerAttackGrid playerFlexCol">
            <div className="border">
                <Char_Weapon />
                <Char_Weapon />
                <Char_Weapon />
            </div>
        </div>
    )
};

export default charAttack;