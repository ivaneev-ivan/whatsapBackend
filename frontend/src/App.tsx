import { MantineProvider } from '@mantine/core'
import '@mantine/core/styles.css'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Home from './pages/Home'
const App = () => {
	return (
		<MantineProvider>
			<BrowserRouter>
				<Routes>
					<Route index element={<Home />} />
				</Routes>
			</BrowserRouter>
		</MantineProvider>
	)
}

export default App
