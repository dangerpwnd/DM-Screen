import React from "react"
import CharImg from "./char_img"
import CharName from "./char_name"
import CharClass from "./char_class"
import CharSpeed from "./char_speed"
import CharAc from "./char_ac"
import CharAttr from "./char_attr"
import CharHp from "./char_hp"
import CharDeathSave from "./char_deathsave"
import CharModifier from "./char_modifier"
import CharSkill from "./char_skill"
import CharAttack from "./char_attack"
import CharFeat from "./char_feat"
import CharEquip from "./char_equip"
import CharCoin from "./char_coin"
import Characteristics from "./characteristics"
import CharNotes from "./char_notes"

function PlayerDetail() {
    return(
        <div>
            <div className="playerDetailGrid">
                <CharImg />
                <CharName />
                <CharClass />
                <CharSpeed />
                <CharAc />
                <CharAttr />
                <CharHp />
                <CharDeathSave />
                <CharModifier />
                <CharSkill />
                <CharAttack />
                <CharFeat />
                <CharEquip />
                <CharCoin />
                <Characteristics />
                <CharNotes />
            </div>
        </div>
    )
}

export default PlayerDetail
