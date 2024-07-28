import { Button, Flex, Input, Table, Textarea } from '@mantine/core'
import { FC, useState } from 'react'
import { Link } from 'react-router-dom'
import Layout from '../components/Layout'

interface Element {
	phone: string
	sendLimitFrom: number
	sendLimitTo: number
	autoLimitFrom: number
	autoLimitTo: number
	progrevFrom: number
	progrevTo: number
	callFrom: number
	callTo: number
	percentProgrev: number
	status: string
	note: string
}
const elements = [
	{
		phone: '+79952680545',
		sendLimitFrom: 10,
		sendLimitTo: 20,
		autoLimitFrom: 10,
		autoLimitTo: 30,
		progrevFrom: 10,
		progrevTo: 10,
		callFrom: 10,
		callTo: 20,
		percentProgrev: 20,
		status: 'Нажатие на кнопку отправелние',
		note: '',
	},
	{
		phone: '+79952680545',
		sendLimitFrom: 10,
		sendLimitTo: 20,
		autoLimitFrom: 10,
		autoLimitTo: 30,
		progrevFrom: 10,
		progrevTo: 10,
		callFrom: 10,
		callTo: 20,
		percentProgrev: 20,
		status: 'send',
		note: '',
	},
	{
		phone: '+79952680545',
		sendLimitFrom: 10,
		sendLimitTo: 20,
		autoLimitFrom: 10,
		autoLimitTo: 30,
		progrevFrom: 10,
		progrevTo: 10,
		callFrom: 10,
		callTo: 20,
		percentProgrev: 20,
		status: '',
		note: '',
	},
	{
		phone: '+79952680545',
		sendLimitFrom: 10,
		sendLimitTo: 20,
		autoLimitFrom: 10,
		autoLimitTo: 30,
		progrevFrom: 10,
		progrevTo: 10,
		callFrom: 10,
		callTo: 20,
		percentProgrev: 20,
		status: '',
		note: '',
	},
]

const GetRow: FC<Element> = element => {
	const [data, setData] = useState<Element>(element)

	return (
		<Table.Tr key={data.phone}>
			<Table.Td>
				<Link to='#'>{data.phone}</Link>
			</Table.Td>
			<Table.Td>
				<Flex gap='xs'>
					<Input value={data.sendLimitFrom} />
					<Input value={data.sendLimitTo} />
				</Flex>
			</Table.Td>
			<Table.Td>
				<Flex gap='xs'>
					<Input value={data.autoLimitFrom} />
					<Input value={data.autoLimitTo} />
				</Flex>
			</Table.Td>
			<Table.Td>
				<Flex gap='xs'>
					<Input value={data.progrevFrom} />
					<Input value={data.progrevTo} />
				</Flex>
			</Table.Td>
			<Table.Td>
				<Flex gap='xs'>
					<Input value={data.callFrom} />
					<Input value={data.callTo} />
				</Flex>
			</Table.Td>
			<Table.Td>{data.status}</Table.Td>
			<Table.Td>
				<Textarea value={data.note} />
			</Table.Td>
			<Table.Td>
				<Button variant='filled' color='red'>
					X
				</Button>
			</Table.Td>
		</Table.Tr>
	)
}

const Home = () => {
	const rows = elements.map(element => GetRow(element))
	return (
		<Layout>
			<Table highlightOnHover withTableBorder withColumnBorders>
				<Table.Thead>
					<Table.Tr>
						<Table.Th>Номер тел.</Table.Th>
						<Table.Th>Рассылка (лимиты)</Table.Th>
						<Table.Th>Автоответчик (лимиты)</Table.Th>
						<Table.Th>Прогрев сообщ. (лимиты на отпр.)</Table.Th>
						<Table.Th>Прогрев исх. звон.</Table.Th>
						<Table.Th>Статус того что делает телефон</Table.Th>
						<Table.Th>Примечание</Table.Th>
						<Table.Th></Table.Th>
					</Table.Tr>
				</Table.Thead>
				<Table.Tbody>{rows}</Table.Tbody>
			</Table>
		</Layout>
	)
}

export default Home
