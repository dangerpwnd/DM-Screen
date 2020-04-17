import React from "react"
import CharImg from "./char_img"
import CharMain from "./char_main"
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
                <CharMain />
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
