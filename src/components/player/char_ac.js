import React from "react";

const charAc = (props) => {
    const ac = props.ac;
    const reg = ac.base + ac.nat + ac.dex + ac.armor + ac.magic;
    const flatFoot = ac.base + ac.nat + ac.armor + ac.magic;
    const touch = ac.base + ac.nat + ac.dex + ac.magic;

    return(
        <div>
            <div className="border playerFlexRow">
                <h3>Regular: {reg}</h3>
                <h3>Flat-footed: {flatFoot}</h3>
                <h3>Touch: {touch}</h3>
            </div>
        </div>
    )
};

export default charAc;