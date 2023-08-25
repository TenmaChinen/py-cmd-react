import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Base from './routes/base/Base'
import Home from './routes/home/Home'
import Foo from './routes/foo/Foo'

export default function App() {
	return (
		<Routes>
			<Route path='/' element={<Base />}>
				<Route path='home' element={<Home />} />
				<Route path='foo' element={<Foo />} />
			</Route>
		</Routes>
	);
}