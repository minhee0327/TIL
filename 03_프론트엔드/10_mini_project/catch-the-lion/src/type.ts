//타입 정의하는 파일
export interface Hello {
    text: string;
}

export const User = {
    name: 'user1',
};

type d = Hello & { hi(): void };

export default d;
