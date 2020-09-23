import React from "react";
import char_Weapon from "./char_weapon";

const charAttack = () => {
    return(
        <div className="playerAttackGrid playerFlexCol">
            <div className="border">
                <char_Weapon />
                <char_Weapon />
                <char_Weapon />
            </div>
        </div>
    )
};

export default charAttack;