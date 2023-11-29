import { useEffect } from 'react';

const Caspio = ({ appKey, account, caspioDiv, classItem, paramTitle, param }) => {
    useEffect(() => {
        if (!document.getElementById(caspioDiv + '-script')) {
            appendScript(appKey, account, caspioDiv, paramTitle, param)
        }

    }, [param]);

    return (
        <div className={classItem} id={caspioDiv}></div>
    )

};

function appendScript(appKey, account, caspioDiv, paramTitle, param) {
    const s = document.createElement('script');
    s.type = 'text/javascript'
    s.id = caspioDiv + '-script'
    const p = `?${paramTitle}=${param}`
    s.src = `https://${account}.caspio.com/dp/${appKey}/emb${p}`;
    try {
        document.getElementById(caspioDiv).appendChild(s);
    } catch { }
}

export default Caspio;