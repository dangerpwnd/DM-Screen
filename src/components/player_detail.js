import React from "react"
import Char_Img from "./char_img"
import Char_Name from "./char_name"
import Char_Class from "./char_class"
import Char_Speed from "./char_speed"
import Char_AC from "./char_ac"
import Char_Attr from "./char_attr"
import Char_HP from "./char_hp"
import Char_DeathSave from "./char_deathsave"
import Char_Modifier from "./char_modifier"
import Char_Skill from "./char_skill"
import Char_Attack from "./char_attack"
import Char_Feat from "./char_feat"
import Char_Equip from "./char_equip"
import Char_Coin from "./char_coin"
import Characteristics from "./characteristics"
import Char_Notes from "./char_notes"

function Player_Detail() {
    return(
        <div>
            <div className="playerDetailGrid">
                <Char_Img />
                <Char_Name />
                <Char_Class />
                <Char_Speed />
                <Char_AC />
                <Char_Attr />
                <Char_HP />
                <Char_DeathSave />
                <Char_Modifier />
                <Char_Skill />
                <Char_Attack />
                <Char_Feat />
                <Char_Equip />
                <Char_Coin />
                <Characteristics />
                <Char_Notes />
            </div>
        </div>
    )
}

export default Player_Detail
