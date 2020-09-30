import React from "react";
import CharWeapon from "./char_weapon";

const charAttack = () => {
    return(
        <div className="playerAttackGrid playerFlexCol">
            <div className="border">
                <CharWeapon />
                <CharWeapon />
                <CharWeapon />
            </div>
        </div>
    )
};

export default charAttack;