import { MenuData } from './store.js';

const MENU = "menus.json";
const VERSION = "menus.version";

function getFromServer(newVersion){
    fetch(MENU).then((resp) => resp.json()).then((data) => {
        // 스토어에 저장
        MenuData.set(data);
        // 로컬 스토리지에 캐시 저장
        localStorage.setItem(MENU, JSON.stringify(data));
        localStorage.setItem(VERSION, newVersion);
    });
}

export function getMenus(){
    let thisVersion = localStorage.getItem(VERSION);

    fetch(VERSION).then((resp) => resp.text()).then((data) => {
        if(thisVersion === data){
            // 로컬 스토리지에서 값 불러오기
            MenuData.set(
                JSON.parse(localStorage.getItem(MENU))
            );
        } else {
            // 메뉴 데이터 업데이트
            getFromServer(data);
        }
    });
}
