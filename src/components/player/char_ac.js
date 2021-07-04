import React from "react";

const charAc = (props) => {

    const { base, nat, dex, armor, magic} =  props;
    const reg = base + nat + dex + armor + magic;
    const flatFoot = base + nat + armor + magic;
    const touch = base + nat + dex + magic;

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