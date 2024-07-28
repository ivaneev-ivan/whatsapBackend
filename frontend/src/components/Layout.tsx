import { FC, ReactNode } from 'react'
import HeaderMenu from './Header/Header'

export interface Child {
	children: ReactNode
}

const Layout: FC<Child> = ({ children }) => {
	return (
		<>
			<HeaderMenu />
			<div style={{ margin: '0 50px' }}>{children}</div>
		</>
	)
}

export default Layout
